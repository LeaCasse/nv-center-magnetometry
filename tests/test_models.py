import numpy as np
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from nvcenter_stage.models import lorentzian, saturation_model
from nvcenter_stage.stripe import stripe_field_projection

def test_lorentzian_center_is_dip():
    freq = np.linspace(-1.0, 1.0, 101)
    y = lorentzian(freq, 0.0, 0.5, 0.2, 10.0)
    assert y[50] < y[0]

def test_saturation_model_is_monotonic():
    p = np.array([1.0, 10.0, 100.0])
    y = saturation_model(p, 100.0, 50.0)
    assert np.all(np.diff(y) > 0)

def test_stripe_projection_shape():
    x = np.linspace(-1e-6, 3e-6, 10); z = np.zeros_like(x) + 50e-9
    b = stripe_field_projection(x, z, x1_m=0.0, z_offset_m=50e-9, theta_deg=54.7, phi_deg=0.0)
    assert b.shape == x.shape
