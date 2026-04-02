import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
for script in ['build_dataset_inventory.py', 'analyze_confocal_filters.py', 'analyze_odmr_grid.py', 'fit_single_odmr_example.py']:
    subprocess.run([sys.executable, str(ROOT / 'scripts' / script)], check=True)
