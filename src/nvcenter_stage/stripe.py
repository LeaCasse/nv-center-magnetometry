import numpy as np
from scipy.optimize import curve_fit
MU0 = 1.2566370614e-6

def fit_linear_background(x, z, edge_points=30):
    x_out = np.concatenate((x[:edge_points], x[-edge_points:]))
    z_out = np.concatenate((z[:edge_points], z[-edge_points:]))
    def linear(xx, a, b):
        return a * xx + b
    popt, _ = curve_fit(linear, x_out, z_out, p0=[0.0, float(np.median(z_out))])
    return linear(x, *popt), popt

def bx_stripe(x_m, z_m, x1_m, width_m, ms_a_per_m, thickness_m):
    pref = (MU0 * ms_a_per_m * thickness_m) / (2.0 * np.pi)
    return -pref * (z_m / ((x_m - x1_m) ** 2 + z_m**2)) + pref * (z_m / ((x_m - x1_m - width_m) ** 2 + z_m**2))

def bz_stripe(x_m, z_m, x1_m, width_m, ms_a_per_m, thickness_m):
    pref = (MU0 * ms_a_per_m * thickness_m) / (2.0 * np.pi)
    return pref * ((x_m - x1_m) / ((x_m - x1_m) ** 2 + z_m**2)) - pref * ((x_m - x1_m - width_m) / ((x_m - x1_m - width_m) ** 2 + z_m**2))

def stripe_field_projection(x_m, z_m, x1_m, z_offset_m, theta_deg, phi_deg, width_m=2e-6, ms_a_per_m=1e6, thickness_m=1e-9):
    theta = np.deg2rad(theta_deg); phi = np.deg2rad(phi_deg)
    effective_z = z_offset_m + z_m
    bx = bx_stripe(x_m, effective_z, x1_m, width_m, ms_a_per_m, thickness_m)
    bz = bz_stripe(x_m, effective_z, x1_m, width_m, ms_a_per_m, thickness_m)
    return np.sin(theta) * np.cos(phi) * bx + np.cos(theta) * bz
