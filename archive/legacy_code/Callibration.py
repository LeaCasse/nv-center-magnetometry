import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, a, b):
    return a*x+b

#Data exportation
b_field = np.loadtxt('C:\\Users\\L&a\\Documents\\Fac\\M1\\Stage\\Callibrage\\fullbscan\\11\\Plot\\b_fied_1646-42.dat')
height = np.loadtxt('C:\\Users\\L&a\\Documents\\Fac\\M1\\Stage\\Callibrage\\fullbscan\\11\\Plot\\height_1646-42.dat')

#Gauss to miliTesla convertion
b_field= b_field/10 

reffreq = 2755 

refb = (2870 - reffreq )/28

b_field= b_field - refb

profil_field = b_field[:,-4]
profil_height = height[:,-4]

x = np.linspace(0,5, 120)
z = profil_height

x_out = np.concatenate((x[:30],x[-30:]))
z_out = np.concatenate((z[:30],z[-30:]))

p_opt, p_cov = curve_fit(linear, x_out, z_out , p0=[0.5E-7, 0.5E-7])

fit_topo = linear(x,*p_opt)

#plt.figure()
#plt.imshow(b_field)
#plt.colorbar()

#plt.figure()
#plt.plot(x,profil_height-fit_topo-1E-8)
#plt.plot(x,fit)

"Bx et By pour trouver B_NV et pouvoir fiter notre champs magnétique :"

t = 1e-9
mu_0 = 1.2566370614E-6
w=2E-6
M_S = 1E6

topo = profil_height-fit_topo-1E-8
x_prof = x*1E-6

#z_opt = z
#print(z_opt)

def Bx(w, M_S, x_prof, z_opt, x1):
    return - ((mu_0 * M_S * t ) / ( 2 * np.pi ))*( z_opt / ((x_prof-x1)**2 + z_opt**2)) + ((mu_0 * M_S * t ) / ( 2 * np.pi ))*( z_opt / ((x_prof-x1-w)**2 + z_opt**2))

def Bz(w, M_S, x_prof, z_opt, x1):
    return + ((mu_0 * M_S * t ) / ( 2 * np.pi ))*( (x_prof-x1) / ((x_prof-x1)**2 + z_opt**2)) - ((mu_0 * M_S * t ) / ( 2 * np.pi ))*( (x_prof-x1-w) / ((x_prof-x1-w)**2 + z_opt**2))

def B_NV(x_prof, z_opt, x1, theta, phi):
    t = theta*np.pi/180 
    p = phi*np.pi/180 
    return np.sin(t) * np.cos(p) * Bx(w, M_S, x_prof, z_opt+topo, x1) + np.cos(t) * Bz(w, M_S, x_prof , z_opt+topo, x1)

p0 = [ 5E-8, 1.45E-6, 58, -2]
P_opt, P_cov = curve_fit(B_NV, x_prof, profil_field*1E-3 , p0=p0, 
                         bounds=([ 2E-8, 1.2E-6, 35 , -20],[ 2E-7, 1.7E-6, 70, 20] ))

print(P_opt)

fit_B_NV = B_NV(x_prof, *P_opt)
init_B_NV = B_NV(x_prof, *p0)

plt.figure()
plt.plot(x_prof,profil_field, label='experimental profil field')
plt.plot(x_prof,fit_B_NV*1E3, label= 'fitted profil field')
plt.xlabel('Y axis (in nm)' )
plt.ylabel('Magnetic field (in miliTesla)')
plt.legend()
#plt.title("Magnetic field measurement above a uniformly magnetized magnetic stripe" )
plt.savefig('exp.png', format='png', dpi=300)
#plt.plot(x_prof,init_B_NV*1E3)

