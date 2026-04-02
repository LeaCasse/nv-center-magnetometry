# Magnetic-stripe calibration status

The original internship report contains a clear spatial-resolution and flight-height calibration narrative based on edge fields above a uniformly magnetized stripe.

## What the report states

- the calibrated tip is **FR076-9C-3B17**;
- the sample used for calibration is a patterned magnetic sample referred to in the report as **Hayashi-C PRB94, 064413**;
- quenching scans were first used to identify cleaner regions of the magnetic tracks;
- scans were then discussed both **with** and **without** an additional bias magnet;
- the final goal was to fit the measured magnetic profile with an analytical stripe-edge model to infer the NV-axis orientation and the tip flight height.

## Why this folder is still mostly documentation

The accessible material includes:

- the report,
- the presentation slides,
- calibration PDFs,
- the legacy script `archive/legacy_code/Callibration.py`.

However, the exact raw arrays used by the calibration script (`b_field`, `height`) were not recoverable from the uploaded material. Because of that, this repository does **not** claim a fully reproducible magnetic-stripe re-fit.

## Practical consequence

This repository should be understood as:

- **fully reusable** for the confocal and ODMR parts,
- **partially documented but not fully reproducible** for the final stripe-fit / flight-height extraction.
