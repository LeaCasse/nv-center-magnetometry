from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import numpy as np

from .paths import DATA_RAW


@dataclass
class ConfocalScan:
    folder: Path
    metadata: Dict[str, str]
    table: np.ndarray
    image: np.ndarray | None


@dataclass
class OdmrSpectrum:
    folder: Path
    channel: str
    range_name: str
    data: np.ndarray


def _parse_header_metadata(path: Path) -> Dict[str, str]:
    metadata: Dict[str, str] = {}
    with path.open('r', encoding='utf-8', errors='ignore') as handle:
        for line in handle:
            if not line.startswith('#'):
                break
            if ':' in line:
                raw = line[1:].strip()
                if raw.startswith('Saved Data'):
                    metadata['saved_data'] = raw
                    continue
                key, value = raw.split(':', 1)
                metadata[key.strip()] = value.strip()
    return metadata


def load_confocal_scan(folder: Path) -> ConfocalScan:
    data_file = next(folder.glob('*_confocal_xy_data.dat'))
    image_file = next(folder.glob('*_confocal_xy_image_Dev1Ctr0.dat'), None)
    metadata = _parse_header_metadata(data_file)
    table = np.loadtxt(data_file, comments='#')
    image = np.loadtxt(image_file, comments='#') if image_file else None
    return ConfocalScan(folder, metadata, table, image)


def load_odmr_spectrum(path: Path) -> OdmrSpectrum:
    rows = []
    with path.open('r', encoding='utf-8', errors='ignore') as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            parts_line = stripped.replace(',', ' ').split()
            if len(parts_line) < 2:
                continue
            try:
                rows.append([float(parts_line[0]), float(parts_line[1])])
            except ValueError:
                continue
    data = np.array(rows, dtype=float)
    parts = path.stem.split('_')
    channel = next((p for p in parts if p.startswith('ch')), 'unknown')
    range_name = next((p for p in parts if p.startswith('range')), 'unknown')
    return OdmrSpectrum(path.parent, channel, range_name, data)


def discover_confocal_scans(base: Path | None = None) -> List[Path]:
    base = base or (DATA_RAW / 'confocal')
    return sorted([p for p in base.iterdir() if p.is_dir()])


def discover_odmr_spectra(base: Path | None = None) -> List[Path]:
    base = base or (DATA_RAW / 'odmr')
    paths: List[Path] = []
    for folder in sorted([p for p in base.iterdir() if p.is_dir()]):
        paths.extend(sorted(folder.glob('*_ODMR_data_ch*_range*.dat')))
    return paths
