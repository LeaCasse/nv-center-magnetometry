# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:13:36 2022

@author: L&a
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def lorentzian(freq, f0, delta, amplitude, offset) : 
    return offset*(1-amplitude/ (1 + ((freq-f0)/(delta/2))**2))

# Recuperation des données
datapath = r"C:\\Users\\L&a\\Documents\\Fac\\M1\\Stage\\Sensitivity\\ODMR\\"

rf=np.array([15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
time=np.array(['1507-36','1511-34','1513-02','1514-45',
               '1516-18','1517-43','1518-51','1519-51','1520-52',
               '1522-18','1523-56','1524-52','1525-46','1526-35','1527-30'])

# Initialisation des données 
largeur=np.zeros(len(rf))
contrast=np.zeros(len(rf))
offset=np.zeros(len(rf))
error_largeur=np.zeros(len(rf))
error_contrast=np.zeros(len(rf))
error_offset=np.zeros(len(rf))

for i in range(len(rf)):
    spectre = np.loadtxt(f"{datapath}20220518-{time[i]}_ODMR_data_ch0.dat")
    Popt, Pcov = curve_fit(lorentzian, spectre[:,0], spectre[:,1], 
                           p0=[2.83E+9, 10E+6, 0.1, np.max(spectre[:,1])])
    #print(Popt)
    PLfit = lorentzian(spectre[:,0], *Popt)
    PL_init = lorentzian(spectre[:,0], 2.83E+9, 10E+6, 0.1, np.max(spectre[:,1]))
    largeur[i]=Popt[1]
    contrast[i]=Popt[2]
    offset[i]=Popt[3]
    error=np.sqrt(np.diag(Pcov))
    error_largeur[i]=error[1]
    error_contrast[i]=error[2]
    error_offset[i]=error[3]
    
    plt.figure('Fluorescence as a function of microwave power') 
    plt.xlabel(r'rf power (dBm)')
    plt.ylabel('Fluorescence (kcount/s)')
    plt.title('Fluorescence as a function of microwave power')
    plt.plot(spectre[:,0],spectre[:,1])
   #plt.plot(spectre[:,0],PL_init)
    plt.plot(spectre[:,0], PLfit, c="blue", label="PLfit(t)")  
    
#Sensitivity
Pl = 4/(3*np.sqrt(3))
h = 6.62607015E-34      # cte de planck 
g  = 2.0023             # facteur de landé 
mu = 9.27400949E-24     # magneton de bhor 

#conversion dBm en omega_R
rf_W=10*np.log(rf)
s=317/114

def fit_contrast(rf_W,A,theta,gamma):
    return (theta*(A*rf_W))/((A*rf_W) + gamma*(s/(s+1))**2)

Popt, Pcov = curve_fit(fit_contrast, rf_W, contrast ,p0=[10, 0.2, 40E13])
print(Popt)
A = Popt[0]
contrast_fit = fit_contrast(A*np.sqrt(rf_W), *Popt)
contrast_init = fit_contrast(A*np.sqrt(rf_W), 1000, 0.2, 40E13)

#Plot du contrast
plt.figure('Contrast as a function of microwave power') 
plt.xlabel(r'Microwave power ($\omega_{R}$)')
plt.ylabel('Contrast (in percent)') 
plt.title('Contrast as a function of microwave power')   
plt.errorbar(A*np.sqrt(rf_W),contrast,yerr=error_contrast,fmt='.')
plt.plot(A*np.sqrt(rf_W),contrast_init)
plt.plot(A*np.sqrt(rf_W), contrast_fit, c="green", label="contrastfit(t)") 
plt.xscale('log')
plt.show()


sensitivity=(Pl*h*np.abs(largeur))/(g*mu*contrast*np.sqrt(offset))
#error_sensitivity = ((error_largeur)/(contrast*np.sqrt(offset))) + ((np.abs(largeur)*error_offset)/(contrast*(offset**(3/2))) + ((np.abs(largeur)*error_contrast)/(np.sqrt(offset)*(contrast**2))))


plt.figure('Sensitivity as a function of microwave power')    
#plt.errorbar(laser/114,sensitivity,yerr=error_sensitivity,fmt='.')
#plt.xscale('log')
plt.plot(A*np.sqrt(rf_W),sensitivity,'.')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'Microwave power ($\omega_{R}$)')
plt.ylabel(r'Magnetic sensitivity ($\frac{T}{\sqrt{Hz}}$)')
plt.title('Sensitivity as a function of microwave power')