# Repository guide

## Design choices

This repo separates the material into three layers:

1. **raw data**: kept close to the original exports;
2. **legacy artifacts**: original scripts and notes, untouched;
3. **clean analysis layer**: reusable package + scripts.

That separation matters. The original internship material was useful, but not clean enough for direct reuse.

## Folder naming

Some source folders contained accents, spaces, or scanner-escaped unicode fragments such as `#U00b0`. Those were normalized into ASCII-safe GitHub-friendly names. The original-to-sanitized mapping is preserved in:

- `data/raw/confocal/_folder_map.csv`
- `data/raw/odmr/_folder_map.csv`

## Recommended workflow

### To inspect the raw material
Start from:

- `data/raw/presentation/`
- `data/raw/odmr/`
- `data/raw/confocal/`
- `archive/legacy_code/`

### To run the cleaned analysis
Use:

```bash
python scripts/build_all.py
```

### To extend the project
The most natural next extensions would be:

- adding a more robust double-Lorentzian model selection for split ODMR lines,
- reconstructing the magnetic-stripe calibration if the original `b_field` and `height` maps are recovered,
- adding a notebook that narrates the full workflow pedagogically.


## Additional note after integrating the final report

The repository now includes the original French internship report in `data/raw/report/stage_report_fr.pdf`.

That report is not just archival. It resolves several ambiguities from the raw folders:

- why the project is best framed around **magnetometry** rather than generic NV physics,
- why the **Qnami ProteusQ** setup is the main experimental reference,
- why the spatial-resolution part should be treated as **documented but only partially reproducible**,
- which quantitative values are safe to quote when presenting the internship.

Use `docs/report_crosswalk.md` if you need to move back and forth between the report narrative and the cleaned repository.
