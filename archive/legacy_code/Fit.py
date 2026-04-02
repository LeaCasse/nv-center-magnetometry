# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('C:\\Users\\lea\\Downloads\\20220511-1646-42_b_field_fw.dat')

data= data/10 #converti en miliTesla

reffreq = 2755 

refb = (2870 - reffreq )/28

data= data - refb

profil = data[:,-3]

x = np.linspace(0,5, 120)

plt.figure()
plt.imshow(data)
plt.colorbar()

plt.figure()
plt.plot(x,profil)