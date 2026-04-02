# NV-center internship archive

This repository reorganizes a first-year Master's internship on **NV-center-based quantum sensing**.

The original material mixed raw microscope exports, ODMR scans, presentation slides, exploratory scripts, notes, screenshots, and large image dumps... all of this in french. This repo keeps the pieces that are directly useful for understanding and reusing the project:

- **raw confocal data** for several collection/filter configurations,
- **raw ODMR spectra** across microwave power and waveplate-angle settings,
- **stage notes and calibration PDFs**,
- **presentation slides exported as PNGs**,
- **legacy exploratory code**, preserved in `archive/legacy_code/`,
- **clean analysis code** in `src/nvcenter_stage/`,
- **recomputed summaries and figures** in `results/`.

## Scientific scope

The internship was centered on **NV-center magnetometry** and the work eventually relied on the **commercial Qnami ProteusQ** setup after a technical issue on the in-house objective, and the main calibrated tip was **FR076-9C-3B17**. The main themes were:

1. understanding the NV center as a room-temperature quantum sensor,
2. optimizing fluorescence collection with different confocal/filter configurations and fiber alignment,
3. characterizing ODMR lineshapes and their dependence on laser / microwave settings,
4. estimating magnetic sensitivity from contrast, linewidth, and photoluminescence,
5. documenting the spatial-resolution / flight-height calibration workflow above a magnetic stripe.

## Repository layout

```text
nv-center-stage/
├── README.md
├── pyproject.toml
├── requirements.txt
├── src/nvcenter_stage/         # clean reusable Python package
├── scripts/                    # reproducible entry points
├── tests/                      # light sanity checks
├── data/raw/
│   ├── confocal/               # raw confocal exports (+ folder map)
│   ├── odmr/                   # raw ODMR spectra and notes (+ folder map)
│   ├── presentation/           # slide PNGs and exported calibration notes
│   └── notes/                  # reserved for extra notes if extended later
├── results/
│   ├── confocal/
│   ├── odmr/
│   └── magnetic_stripe/
├── docs/
│   ├── stage_summary.md
│   ├── repository_guide.md
│   ├── dataset_inventory.csv
│   └── assets/
└── archive/
    ├── legacy_code/            # original scripts as received
    └── legacy_notes/
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/build_all.py
pytest -q
```

## Reproducible outputs

The main generated artifacts are:

- `results/confocal/confocal_summary.csv`
- `results/confocal/confocal_max_counts.png`
- `results/odmr/odmr_summary_ch0.csv`
- `results/odmr/odmr_condition_map.png`
- `results/odmr/odmr_best_conditions.csv`
- `results/odmr/odmr_fit_example_18dbm_60deg.png`
- `results/magnetic_stripe/README.md`

The original report also states explicit reference values that are useful when presenting the project:

- saturation fit: `I0 = 180.31 kcounts/s`
- saturation power: `Psat = 114.64 µW`
- best sensitivity reported on the Qnami setup: `5.762 µT / sqrt(Hz)`
