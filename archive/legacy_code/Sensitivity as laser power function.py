# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:00:21 2022

@author: L&a
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def lorentzian(freq, f0, delta, amplitude, offset) : 
    return offset*(1-amplitude/ (1 + ((freq-f0)/(delta/2))**2))

# Recuperation des données
datapath = r"C:\\Users\\L&a\\Documents\\Fac\\M1\\Stage\\Sensitivity\\ODMR\\"

laser=np.array([1.05,1.39,1.74,2.01,2.28,2.50,2.66,3.32,4.1,6.671,14,24,30,43,50,62,73,81,88.3,103,125,134.2,171,200,250,317,412,421,579,669,765,889])
time=np.array(['1408-12','1413-27','1416-51','1419-36','1421-33','1423-46','1425-25','1427-07','1429-19','1430-56','1432-57','1435-10','1437-55','1439-38','1440-58','1442-24','1444-00','1445-22','1446-40','1447-58','1449-30','1450-53','1452-17','1453-42','1454-56',
      '1456-06','1457-35','1459-02','1500-20','1501-49','1501-50','1502-57','1507-36','1511-34'])

# Initialisation des données 
largeur=np.zeros(len(laser))
contrast=np.zeros(len(laser))
offset=np.zeros(len(laser))
error_largeur=np.zeros(len(laser))
error_contrast=np.zeros(len(laser))
error_offset=np.zeros(len(laser))

for i in range(len(laser)):
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
    
    plt.figure('Fluorescence as a function of laserpower') 
    plt.xlabel(r'Laser power ($\mu$ W)')
    plt.ylabel('Fluorescence (kcount/s)')
    plt.title('Fluorescence as a function of laserpower')
    plt.plot(spectre[:,0],spectre[:,1])
   #plt.plot(spectre[:,0],PL_init)
    plt.plot(spectre[:,0], PLfit, c="blue", label="PLfit(t)") 
       
plt.show() 

#Plot du contrast
plt.figure('Contrast as a function of laserpower') 
plt.xlabel(r's ($=\frac{P_{laser}}{P_{SAT}}$) ($\mu$ W)')
plt.ylabel('Contrast (in percent)') 
plt.title('Contrast as a function of laserpower')   
plt.errorbar(laser/114,contrast,yerr=error_contrast,fmt='.')
plt.xscale('log')
plt.show() 

#Plot de la largeur
plt.figure('Largeur FWHM as a function of laserpower') 
plt.xlabel(r's ($=\frac{P_{laser}}{P_{SAT}})$ ($\mu$ W)')
plt.ylabel('Largeur FWHM (in Hz)')  
plt.title('Largeur FWHM as a function of laserpower')  
plt.errorbar(laser/114,np.abs(largeur),yerr=error_largeur,fmt='.')
plt.xscale('log')
plt.show() 

#Plot de la photoluminescence
plt.figure('Photoluminescence as a function of laserpower') 
plt.xlabel(r's ($=\frac{P_{laser}}{P_{SAT}})$  ($\mu$ W)')
plt.ylabel('Photoluminescence (in kcount/s)')
plt.title('Photoluminescence as a function of laserpower')   
plt.errorbar(laser/114,offset,yerr=error_offset,fmt='.')
plt.xscale('log')
plt.show() 
    
#Sensitivity
Pl = 4/(3*np.sqrt(3))
h = 6.62607015E-34      # cte de planck 
g  = 2.0023             # facteur de landé 
mu = 9.27400949E-24     # magneton de bhor 

sensitivity=(Pl*h*np.abs(largeur))/(g*mu*contrast*np.sqrt(offset))
#error_sensitivity = ((error_largeur)/(contrast*np.sqrt(offset))) + ((np.abs(largeur)*error_offset)/(contrast*(offset**(3/2))) + ((np.abs(largeur)*error_contrast)/(np.sqrt(offset)*(contrast**2))))

plt.figure('Sensitivity as a function of laserpower')    
#plt.errorbar(laser/114,sensitivity,yerr=error_sensitivity,fmt='.')
#plt.xscale('log')
plt.semilog(laser/114,sensitivity,'.')
plt.xlabel(r's ($=\frac{P_{laser}}{P_{SAT}})$ ($\mu$ W)')
plt.ylabel(r' Magnetic sensitivity ($\frac{T}{\sqrt{Hz}}$)')
plt.title('Sensitivity as a function of laserpower')
print('la sensibilté magnétique minimale est:',np.min(sensitivity),'T/sqrt(Hz)')