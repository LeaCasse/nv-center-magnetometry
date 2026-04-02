import pandas as pd
from .io import discover_confocal_scans, discover_odmr_spectra

def build_inventory():
    rows = []
    for folder in discover_confocal_scans(): rows.append({'dataset_type': 'confocal_folder', 'path': str(folder)})
    for spectrum in discover_odmr_spectra(): rows.append({'dataset_type': 'odmr_spectrum', 'path': str(spectrum)})
    return pd.DataFrame(rows)
