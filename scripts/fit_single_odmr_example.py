from pathlib import Path
import sys, matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from nvcenter_stage.io import load_odmr_spectrum
from nvcenter_stage.models import lorentzian
from nvcenter_stage.odmr import fit_single_lorentzian
from nvcenter_stage.plotting import save_current
EXAMPLE = ROOT / 'data' / 'raw' / 'odmr' / '18_dBm_60deg' / '20220428-1016-34_ODMR_data_ch0_range0.dat'

def main():
    spectrum = load_odmr_spectrum(EXAMPLE)
    fit = fit_single_lorentzian(spectrum.data[:,0], spectrum.data[:,1])
    model = lorentzian(spectrum.data[:,0], fit.f0_hz, fit.fwhm_hz, fit.amplitude, fit.offset_counts)
    plt.figure(figsize=(7,4)); plt.plot(spectrum.data[:,0]/1e9, spectrum.data[:,1], 'o', ms=3, label='data'); plt.plot(spectrum.data[:,0]/1e9, model, '-', lw=2, label='single-Lorentzian fit'); plt.xlabel('Frequency (GHz)'); plt.ylabel('Fluorescence (counts/s)'); plt.title('Example ODMR fit: 18 dBm, 60°'); plt.legend(); save_current(ROOT / 'results' / 'odmr' / 'odmr_fit_example_18dbm_60deg.png')
if __name__ == '__main__': main()
