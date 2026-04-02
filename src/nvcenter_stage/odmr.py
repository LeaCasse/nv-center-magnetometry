from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import re
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from .io import load_odmr_spectrum
from .models import lorentzian
@dataclass
class LorentzianFit:
    f0_hz: float
    fwhm_hz: float
    amplitude: float
    offset_counts: float
    contrast: float
    rmse: float

def fit_single_lorentzian(freq_hz, counts):
    guess_f0 = float(freq_hz[np.argmin(counts)])
    guess_delta = float(max((freq_hz.max() - freq_hz.min()) / 10.0, 1e6))
    guess_offset = float(np.max(counts))
    guess_amplitude = float(np.clip((guess_offset - np.min(counts)) / max(guess_offset, 1.0), 1e-4, 0.9))
    p0 = [guess_f0, guess_delta, guess_amplitude, guess_offset]
    lower = [freq_hz.min(), 1e5, 1e-6, 0.0]
    upper = [freq_hz.max(), (freq_hz.max() - freq_hz.min()), 0.95, guess_offset * 10.0]
    popt, _ = curve_fit(lorentzian, freq_hz, counts, p0=p0, bounds=(lower, upper), maxfev=20000)
    fitted = lorentzian(freq_hz, *popt)
    rmse = float(np.sqrt(np.mean((counts - fitted) ** 2)))
    return LorentzianFit(float(popt[0]), float(abs(popt[1])), float(popt[2]), float(popt[3]), float(popt[2]), rmse)

def estimate_sensitivity_t_per_root_hz(fwhm_hz, contrast, offset_counts):
    prefactor = 4.0 / (3.0 * np.sqrt(3.0))
    h = 6.62607015e-34
    g = 2.0023
    mu_b = 9.27400949e-24
    if contrast <= 0 or offset_counts <= 0:
        return float('nan')
    return float(prefactor * h * abs(fwhm_hz) / (g * mu_b * contrast * np.sqrt(offset_counts)))

def parse_condition_from_folder(folder_name):
    clean = folder_name.lower().replace('deg', '°')
    dbm = re.search(r'(\d+)\s*d?bm', clean)
    angle = re.search(r'(\d+)\s*(?:°|deg)', clean)
    return {'condition': folder_name, 'microwave_power_dbm': float(dbm.group(1)) if dbm else np.nan, 'waveplate_angle_deg': float(angle.group(1)) if angle else np.nan}

def summarize_odmr_folder(folder: Path) -> pd.DataFrame:
    rows = []
    for path in sorted(folder.glob('*_ODMR_data_ch*_range*.dat')):
        spectrum = load_odmr_spectrum(path)
        fit = fit_single_lorentzian(spectrum.data[:, 0], spectrum.data[:, 1])
        row = {'folder': folder.name, 'file': path.name, 'channel': spectrum.channel, 'range_name': spectrum.range_name, 'points': int(spectrum.data.shape[0]), **parse_condition_from_folder(folder.name), **asdict(fit), 'estimated_sensitivity_T_per_sqrtHz': estimate_sensitivity_t_per_root_hz(fit.fwhm_hz, fit.contrast, fit.offset_counts)}
        rows.append(row)
    return pd.DataFrame(rows)
