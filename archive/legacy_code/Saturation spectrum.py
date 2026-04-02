# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:02:39 2022

@author: L&a
@title: Laser saturation
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def modele(PLlaser, I0, Psat) : 
    return (I0*PLlaser)/(PLlaser+Psat)

#angle=np.array([37,39,42,44,47,50,52,57,62,67,70,72,74])
PLlaser=np.array([1.05,1.39,1.74,2.01,2.28,2.50,2.66,3.32,4.1,6.671,14,24,30,43,50,62,73,81,88.3,103,125,134.2,171,200,250,317,412,421,579,669,765,889])
PLNV=np.array([1.5,1.9,2.5,2.8,3.1,3.2,4.0,5.0,7.0,38,52,60,62,64,67,70,75,76,76,78,89,93,111,119,124,136,140,146,163,180,185,196])
PLbackground=np.array([0.18,0.2,0.24,0.24,0.24,0.22,0.17,0.25,0.28,0.5,1.61,2.2,2.2,2.4,2.8,3.0,3.1,4.2,7.7,8.2,9,8.7,8.5,9.2,9.0,8.9,9.0,10,15.8,14,15,20])
diff=PLNV-PLbackground

Popt, Pcov = curve_fit(modele, PLlaser, diff, p0=[30,150])
print(Popt)

PLfit = modele(PLlaser, *Popt)

plt.close()
plt.figure('Courbe de saturation de la pointe en fonction de la puissance laser') 
plt.legend()
plt.xlabel(r'Puissance laser ($\mu$W)')
plt.ylabel('Fluorescence (kcount/s)')
plt.title('Courbe de saturation de la pointe en fonction de la puissance laser')
#plt.plot(PLlaser, PLNV)
plt.plot(PLlaser, diff, 'b.')
#plt.plot(PLlaser, PLbackground)
plt.plot(PLlaser, PLfit, c="blue", label="PLfit(t)")
plt.savefig('exp.png', format='png', dpi=300)

plt.show()