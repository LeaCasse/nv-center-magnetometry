# NV-center internship archive and clean re-analysis

This repository reorganizes a first-year Master's internship on **NV-center-based quantum sensing** into a clean, reproducible, English-language GitHub structure.

The original material mixed raw microscope exports, ODMR scans, presentation slides, exploratory scripts, notes, screenshots, and large image dumps. This repo keeps the pieces that are directly useful for understanding and reusing the project:

- **raw confocal data** for several collection/filter configurations,
- **raw ODMR spectra** across microwave power and waveplate-angle settings,
- **stage notes and calibration PDFs**,
- **presentation slides exported as PNGs**,
- **legacy exploratory code**, preserved in `archive/legacy_code/`,
- **clean analysis code** in `src/nvcenter_stage/`,
- **recomputed summaries and figures** in `results/`.

## Scientific scope

The internship was centered on **NV-center magnetometry** rather than quantum computing. According to the original report, the work eventually relied on the **commercial Qnami ProteusQ** setup after a technical issue on the in-house objective, and the main calibrated tip was **FR076-9C-3B17**. The main themes were:

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

## What was deliberately compacted

A large miscellaneous image dump was **not copied wholesale** because much of it was redundant, unrelated, or not needed to understand the stage. Instead, the repo keeps:

- the raw data required for re-analysis,
- the presentation slide exports,
- selected overview contact sheets,
- the original scripts for traceability.

This makes the repository much more usable than a direct archive dump.

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

## Important limitation

The raw **full magnetic-field map** and associated height map used in the original magnetic-stripe calibration script were **not fully recoverable** from the accessible material. The repo therefore preserves the original calibration logic and now also includes the original internship report, but it still does not pretend to fully reproduce the final stripe-fit / flight-height extraction from scratch.

## Why this repo is useful now

This cleaned repository is suitable for:

- showing that you already worked on NV centers experimentally,
- revisiting the internship with a cleaner research workflow,
- sharing a credible technical archive with collaborators,
- extracting a concise technical narrative for future discussions about quantum sensing.
