from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from nvcenter_stage.inventory import build_inventory
if __name__ == '__main__': build_inventory().to_csv(ROOT / 'docs' / 'dataset_inventory.csv', index=False)
