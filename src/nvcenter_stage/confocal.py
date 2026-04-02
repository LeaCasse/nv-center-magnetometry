import numpy as np
import pandas as pd
from .io import load_confocal_scan

def summarize_confocal_folder(folder):
    scan = load_confocal_scan(folder)
    counts = scan.table[:, -1]
    row = {'folder': folder.name, 'num_pixels': int(counts.size), 'min_counts_hz': float(np.min(counts)), 'max_counts_hz': float(np.max(counts)), 'mean_counts_hz': float(np.mean(counts)), 'std_counts_hz': float(np.std(counts)), 'dynamic_range_hz': float(np.max(counts) - np.min(counts))}
    if scan.image is not None:
        row['image_rows'] = int(scan.image.shape[0]); row['image_cols'] = int(scan.image.shape[1])
    for key in ['X image range (m)', 'Y image range (m)', 'XY resolution (samples per range)']:
        if key in scan.metadata:
            row[key] = scan.metadata[key]
    return pd.DataFrame([row])
