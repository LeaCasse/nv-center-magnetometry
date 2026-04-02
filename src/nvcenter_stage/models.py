import numpy as np

def lorentzian(freq, f0, delta, amplitude, offset):
    return offset * (1.0 - amplitude / (1.0 + ((freq - f0) / (delta / 2.0)) ** 2))

def double_lorentzian(freq, f0, f1, delta, amplitude, offset):
    return 0.5 * (lorentzian(freq, f0, delta, amplitude, offset) + lorentzian(freq, f1, delta, amplitude, offset))

def saturation_model(power, i_sat, p_sat):
    return (i_sat * power) / (power + p_sat)
