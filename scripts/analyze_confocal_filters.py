from pathlib import Path
import sys, pandas as pd, matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from nvcenter_stage.io import discover_confocal_scans, load_confocal_scan
from nvcenter_stage.confocal import summarize_confocal_folder
from nvcenter_stage.plotting import save_current

def main():
    rows = [summarize_confocal_folder(folder) for folder in discover_confocal_scans()]
    summary = pd.concat(rows, ignore_index=True).sort_values('max_counts_hz', ascending=False)
    summary.to_csv(ROOT / 'results' / 'confocal' / 'confocal_summary.csv', index=False)
    plt.figure(figsize=(8,4)); plt.bar(summary['folder'], summary['max_counts_hz']); plt.xticks(rotation=45, ha='right'); plt.ylabel('Maximum count rate (Hz)'); plt.title('Confocal comparison across collection/filter configurations'); save_current(ROOT / 'results' / 'confocal' / 'confocal_max_counts.png')
    for folder in discover_confocal_scans():
        scan = load_confocal_scan(folder)
        if scan.image is None: continue
        plt.figure(figsize=(4,4)); plt.imshow(scan.image, origin='lower', aspect='auto'); plt.colorbar(label='Count rate (Hz)'); plt.title(folder.name); save_current(ROOT / 'results' / 'confocal' / f'{folder.name}.png')
if __name__ == '__main__': main()
