"""
Created on Fri Apr 29 09:19:49 2022

@author: L&a
@title: Scan ODMR 
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def lorentzienne(freq, f0, delta, amplitude, offset) : 
    return offset*(1-amplitude/ (1 + ((freq-f0)/(delta/2))**2))
    
def double_lorentzienne(freq, f0, f1, delta, amplitude, offset) : 
    return (lorentzienne(freq,f0, delta, amplitude, offset) + lorentzienne(freq,f1, delta, amplitude, offset) )/2

freq=np.linspace(2850000000,2889900000,58)
PL=np.array([2.969000e+04,2.952500e+04,2.955000e+04,3.054500e+04,3.010000e+04,2.961500e+04,3.004500e+04,2.927000e+04,2.975500e+04,2.908000e+04,2.933000e+04,2.992000e+04,2.870500e+04,2.885500e+04,2.866500e+04,2.859500e+04,2.864500e+04,2.836500e+04,2.725500e+04,2.725500e+04,2.693000e+04,2.680500e+04,2.681000e+04,2.617500e+04,2.745000e+04,2.748500e+04,2.705500e+04,2.734000e+04,2.736500e+04,2.754000e+04,2.719000e+04,2.786500e+04,2.719000e+04,2.649500e+04,2.683000e+04,2.726500e+04,2.798500e+04,2.738500e+04,2.814000e+04,2.811000e+04,2.893500e+04,2.797000e+04,2.904000e+04,2.951000e+04,2.963000e+04,2.880000e+04,3.008000e+04,2.938000e+04,2.946500e+04,2.950500e+04,2.944500e+04,3.011500e+04,2.980500e+04,3.046500e+04,3.007500e+04,3.017500e+04,2.977500e+04,3.047500e+04])

Popt, Pcov = curve_fit(double_lorentzienne, freq, PL, p0=[2.86E+9,2.88E+9, 10E+6, 0.1, 30000])
print(Popt)

PLfit = double_lorentzienne(freq, *Popt)

plt.close()
plt.figure('Scan of NV center fluorescence as a function of the cable signal frequency') 
plt.legend()
plt.xlabel('Fréquency in GHz')
plt.ylabel('Fluorescence in kilocount per seconde')
plt.title('Scan of NV center fluorescence as a function of the cable signal frequency')
plt.plot(freq,PL)
plt.plot(freq, PLfit, c="blue", label="PLfit(t)")
plt.savefig('exp.png', format='png', dpi=300)

plt.show()


