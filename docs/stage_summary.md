# Stage summary

## Short description

This internship focused on the experimental use of **NV centers in diamond as quantum sensors**, mainly for local magnetometry.

## Main technical blocks

### 1. Confocal optimization
Several collection configurations were compared, including different spectral windows, filter choices, and monomode-fiber setups. The goal was not simply to maximize fluorescence, but to improve usable signal quality for ODMR.

### 2. ODMR characterization
A large set of spectra was recorded while changing microwave power and waveplate angle. The relevant observables were:

- resonance frequency,
- linewidth / FWHM,
- ODMR contrast,
- fluorescence offset,
- sensitivity proxy.

### 3. Saturation behavior
The internship included a saturation-curve analysis to estimate fluorescence response versus laser power.

### 4. Magnetic-stripe interpretation
The stage also used a simple analytical model for the magnetic field above a uniformly magnetized stripe. The field was projected onto the NV axis through the usual angular parameters `(theta, phi)`.

## What the internship demonstrates

The material in this repo supports the following statement:

> The internship involved real experimental work on NV-center-based sensing, including confocal imaging, ODMR fitting, signal optimization, and model-based interpretation of magnetic-field measurements.

## What it does *not* demonstrate by itself

The dataset does not support stronger claims such as:

- full sensor fabrication expertise,
- industrial device engineering,
- a complete end-to-end hardware platform.


## Report-informed details added after the initial cleanup

A later pass with the original internship report clarifies several points that were only implicit in the first cleanup:

- the main microscope used for the reported sensitivity and spatial-resolution measurements was the **Qnami ProteusQ** commercial setup;
- the calibrated diamond tip was **FR076-9C-3B17**;
- the internship explicitly separated two performance questions: **magnetic sensitivity** and **spatial resolution / flight height**;
- the report gives a best sensitivity of **5.762 µT / sqrt(Hz)** for the Qnami setup;
- the report documents the use of **quenching scans** to find clean magnetic tracks before field-profile measurements;
- the report discusses scans both with and without an **additional bias magnet**, and stresses that a strong transverse field can make the Zeeman shift non-linear in the measured magnetic field.

## Practical wording that is now justified by the report

A precise one-line description of the internship is now:

> Experimental characterization of an NV-center magnetometer on a Qnami ProteusQ setup, including confocal optimization, ODMR-based sensitivity analysis, and documented stripe-edge calibration workflow for spatial resolution.
