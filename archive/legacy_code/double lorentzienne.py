"""
Created on Fri Apr 29 09:19:49 2022

@author: L&a
@title: Scan ODMR double lorentzienne 
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def lorentzienne(freq, f0, delta, amplitude, offset) : 
    return offset*(1-amplitude/ (1 + ((freq-f0)/(delta/2))**2))
        
def double_lorentzienne(freq, f0, f1, delta, amplitude, offset) : 
    return (lorentzienne(freq,f0, delta, amplitude, offset) + lorentzienne(freq,f1, delta, amplitude, offset) )/2

freq=np.linspace(2850000000,2889900000,58)
PL=np.array([2.081000e+04,2.038500e+04,1.980500e+04,1.993500e+04,1.935000e+04,1.888000e+04,1.931000e+04,1.910000e+04,1.916500e+04,1.867000e+04,1.958500e+04,1.953000e+04,1.949500e+04,2.015500e+04,1.977000e+04,2.035500e+04,2.024500e+04,2.041000e+04,2.081500e+04,2.028000e+04,2.081500e+04,2.078000e+04,2.016500e+04,2.102500e+04,2.102500e+04,2.057500e+04,2.053500e+04,2.163000e+04,2.171500e+04,2.177500e+04,2.087000e+04,2.131500e+04,2.104000e+04,2.116500e+04,2.158500e+04,2.143500e+04,2.084000e+04,2.098500e+04,2.136500e+04,2.056000e+04,1.948500e+04,2.027000e+04,2.052500e+04,1.991000e+04,1.964000e+04,1.856500e+04,1.900500e+04,1.830500e+04,1.817000e+04,1.865000e+04,1.829000e+04,1.899500e+04,1.909000e+04,1.925500e+04,1.934000e+04,2.033000e+04,2.042000e+04,2.126000e+04])

Popt, Pcov = curve_fit(double_lorentzienne, freq, PL, p0=[2.86E+9,2.88E+9, 10E+6, 0.1, 30000])
print(Popt)

PLfit = double_lorentzienne(freq, *Popt)

plt.close()
plt.figure('Scan of NV center fluorescence as a function of the cable signal frequency') 
plt.legend()
plt.xlabel('Fréquency in Hz')
plt.ylabel('Fluorescence in kilocount per seconde')
plt.title('Scan of NV center fluorescence \n as a function of frequency for 25 dBm and 55°')
plt.plot(freq,PL)
plt.plot(freq, PLfit, c="blue", label="PLfit(t)")
plt.savefig('exp.png', format='png', dpi=300)

plt.show()