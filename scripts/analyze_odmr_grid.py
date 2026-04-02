from pathlib import Path
import sys, pandas as pd, matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from nvcenter_stage.odmr import summarize_odmr_folder
from nvcenter_stage.plotting import save_current

def main():
    odmr_root = ROOT / 'data' / 'raw' / 'odmr'
    frames = []
    for folder in sorted([p for p in odmr_root.iterdir() if p.is_dir()]):
        df = summarize_odmr_folder(folder)
        if not df.empty: frames.append(df)
    summary = pd.concat(frames, ignore_index=True)
    summary.to_csv(ROOT / 'results' / 'odmr' / 'odmr_summary_all_channels.csv', index=False)
    ch0 = summary[summary['channel'] == 'ch0'].copy()
    ch0.to_csv(ROOT / 'results' / 'odmr' / 'odmr_summary_ch0.csv', index=False)
    plt.figure(figsize=(7,5)); sc = plt.scatter(ch0['microwave_power_dbm'], ch0['waveplate_angle_deg'], c=ch0['estimated_sensitivity_T_per_sqrtHz'], s=90); plt.xlabel('Microwave power (dBm)'); plt.ylabel('Waveplate angle (deg)'); plt.title('CW-ODMR sensitivity proxy across conditions (channel 0)'); plt.colorbar(sc, label='Estimated sensitivity (T/√Hz)'); save_current(ROOT / 'results' / 'odmr' / 'odmr_condition_map.png')
    ch0.sort_values('estimated_sensitivity_T_per_sqrtHz').head(10).to_csv(ROOT / 'results' / 'odmr' / 'odmr_best_conditions.csv', index=False)
if __name__ == '__main__': main()
