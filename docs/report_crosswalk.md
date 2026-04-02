# Stage report crosswalk

This note links the original French internship report to the cleaned repository structure.

## Report title

**Caractérisation d'un magnétomètre à centre NV**

Master 1 internship supervised at L2C by Vincent Jacques and Aurore Finco, with Guillaume Cassabois as academic tutor.

A copy of the original report is stored in:

- `data/raw/report/stage_report_fr.pdf`

## Main scientific claims from the report

The report makes four central claims that are useful for anyone reading this repository:

1. the internship focused on **NV-center magnetometry** rather than quantum computing;
2. the experimental platform eventually used for the main measurements was the **commercial Qnami ProteusQ microscope**;
3. the tip calibrated in the report is **FR076-9C-3B17**;
4. the internship had two main performance axes: **magnetic sensitivity** and **spatial resolution / flight height**.

## Mapping from report sections to repository content

### Introduction and NV-center theory
These sections are background material. Their role in the repository is mostly documentary.

Most relevant files:
- `data/raw/report/stage_report_fr.pdf`
- `data/raw/presentation/`
- `docs/stage_summary.md`

### Optical path / confocal setup
The report explains the confocal path, dichroic filtering, NV emission filtering, the role of the half-wave plate, and the practical issue that fiber alignment and filtering strongly affect usable fluorescence.

Most relevant files:
- `data/raw/confocal/`
- `scripts/analyze_confocal_filters.py`
- `results/confocal/confocal_summary.csv`
- `results/confocal/confocal_max_counts.png`

### ODMR, saturation, contrast, linewidth, photoluminescence, sensitivity
This is the best reproduced part of the internship in the cleaned repo.

Most relevant files:
- `data/raw/odmr/`
- `archive/legacy_code/Saturation spectrum.py`
- `archive/legacy_code/Sensitivity as a microwave power function.py`
- `archive/legacy_code/Sensitivity as laser power function.py`
- `scripts/analyze_odmr_grid.py`
- `scripts/fit_single_odmr_example.py`
- `results/odmr/odmr_summary_all_channels.csv`
- `results/odmr/odmr_best_conditions.csv`
- `results/odmr/odmr_condition_map.png`
- `results/odmr/odmr_fit_example_18dbm_60deg.png`

### Spatial resolution and magnetic-stripe calibration
The report contains a full physical narrative for stripe-edge magnetometry: quenching scans, sample selection, scans with and without additional bias field, and model-based fitting of the measured edge field to infer the NV-axis geometry and flight height.

What is present in this repo:
- the original calibration logic in `archive/legacy_code/Callibration.py`
- slide exports documenting the stripe model in `data/raw/presentation/`
- calibration PDFs in `data/raw/odmr/`
- a placeholder documentation note in `results/magnetic_stripe/README.md`

What is not fully reproducible from the accessible material:
- the complete raw `b_field` and `height` arrays used by the original calibration script
- the exact end-to-end reconstruction of the final flight-height fit

## Key quantitative values stated in the report

The following numbers appear explicitly in the report and should be used when describing the internship:

- saturation fit: `I0 = 180.31 kcounts/s`
- saturation power: `Psat = 114.64 µW`
- best magnetic sensitivity reported on the Qnami setup: `5.762 µT / sqrt(Hz)`
- vendor specification for the NV depth of tip `FR076-9C-3B17`: `z_N = 9 ± 4 nm`
- typical measured ODMR contrast for that tip during preparation: about `10.5%`

## Interpretation guideline

A careful reading of the report shows that the internship was stronger on:

- understanding the NV sensing principle,
- practical optical alignment and fluorescence collection,
- ODMR-based sensitivity characterization,
- physically informed interpretation of edge-field measurements.

It was weaker on full code reproducibility because the original work mixed exploratory scripts, microscope exports, PDFs, screenshots, and manual notes.
