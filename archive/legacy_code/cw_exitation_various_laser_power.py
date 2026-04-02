import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import pandas as pd 

def lorentzian(x, x0,A0, gamma, y0):
    return A0*((gamma**2)/( gamma**2 +(x-x0)**2 )) +y0

def rebin(dat,nm) :
        N =int(len(dat)/nm)
        new_dat = np.zeros(N)
        for i in range(N) :
            for j in range(nm) :
                 new_dat[i]+=dat[i*nm+j]/nm
        return new_dat

# Parametres initiale pour le fitting

A0 = -0.05     #le contrast en Si (*2 pour %)

gamma = 0.5e7 # la demi largeur de raie a demi-hauteur
 
p0 = [2.705e9, A0 ,gamma,1] #parametre initiale du fit prametré par les parametres initiaux 

plt.figure()


# Recuperation de data 

datapath = r"C:\Users\Elias SFEIR\OneDrive\Desktop\data\Data_TSAR-3I3\ODMR_spectra/"
all_files_name = os.listdir(datapath)
files_name = []
 
for i in range(len(all_files_name )):
    if all_files_name[i][-15:] == "_ch0_range0.dat":
        files_name.append(all_files_name[i])
files_name.sort()   


for j in range(len(files_name)) :
    ODMR_DATA =np.loadtxt(datapath+files_name[j]) 

data = np.loadtxt(r"C:/Users/Elias SFEIR/OneDrive/Desktop/data/Data_TSAR-3I3/laserpower.txt")

# Tableau des points auptimaux avec legend 

B1 = np.ones((len(files_name),len(p0))) # tableau de popt 
B2 = np.ones( (len(files_name),len(p0)) )
a = [100,125,150,175,200,225,250,275,300,350,400,450,500,600,700,800,1000,1290,50,25,75] #tableau de legend


# boucle de data 


for j in range(len(files_name)) :
    ODMR_DATA =np.loadtxt(datapath+files_name[j]) 
    
    frequency =rebin(ODMR_DATA[:,0],5)
    
    signal_PL =rebin(ODMR_DATA[:,1],5)
    
    signal_PL_norm = signal_PL/np.max(signal_PL)
    
    freqfit = np.linspace(frequency[0], frequency[-1], 200)
    
    popt, pcov = curve_fit(lorentzian, frequency, signal_PL_norm, p0)
    B1[j]=popt
    B2[j]=np.diag(pcov)
    fit = lorentzian(freqfit, *popt)
    init= lorentzian(freqfit, *p0)
    
    
    
    color = plt.cm.viridis(j/len(files_name)) 
    plt.plot(frequency*1e-9, signal_PL_norm,'.',label=r"{}uW".format(a[j]),color=color)
    plt.plot(freqfit*1e-9, fit,linewidth=0.5,color=color)
plt.xlabel("Frequency(GHz)")
plt.ylabel(" Normalized Pl(kcounts/s)")
plt.legend(labelspacing=0.1,handletextpad=0.1,fontsize=7.8)


# ##############################################################
# # contrast
# ##############################################################
plt.figure()
plt.plot( a,-B1[:,1]*1e2,'.' )
#plt.title("contraste vs laser power")
plt.ylabel("Contrast (%)")
plt.xlabel("Laser power (\u03bcW)")

###################################################
# largeur mi-hauteur
###################################################
plt.figure()
plt.plot( a,(B1[:,2]/1e6)*2,'.', )
#plt.title("FWHM vs laser power")
plt.ylabel("FWHM (MHz) ")
plt.xlabel("Laser power (\u03bcW)")
###################################################################
# thermal sensitivity
#####################################################################
Contrast =-B1[:,1]
FWHM = B1[:,2]*2
laserpower = data[:,0] #in uW
signal = data[:,1]*1e3
etha= (1/71200)*( FWHM/( Contrast*np.sqrt(signal) ) )  # in k/sqrt(Hz)
plt.figure()
plt.plot(laserpower,etha, '.')
plt.xlabel('Laser power (\u03bcW)')
plt.ylabel('Thermal sensitivity (K/$\sqrt{Hz}$)')
plt.ylim(0,20)
plt.xlim(0,1000)
print('la snesibilté thermique minimal est:',np.min(etha))
###################################################################
#  magnetic sensitivity 
#####################################################################
plt.figure()
# plt.xscale('log')
Contrast =-B1[:,1]
FWHM = B1[:,2]*2
laserpower = data[:,0] #in uW
signal = data[:,1]*1e3
h = 6.6260693*1e-34               # cte de planck 
g  = 2.0023             # facteur de landé 
mu = 9.27400949*1e-24   # magneton de bhor 
etha_mag =  ( h/(g*mu) )*( FWHM/( Contrast*np.sqrt(signal) ) )  # in T/sqrt(Hz) 
plt.plot(laserpower,(etha_mag)*1e6, '.')
plt.xlabel('Laser power (\u03bcW)')
plt.ylabel(' Magnetic sensitivity (\u03bcT/$\sqrt{Hz}$)')
plt.ylim(0,50)
# plt.xlim(0,1000)
print('la sensibilté magnétique minimal est:',np.min(etha_mag))

#####################################################################################
#definition de la fonction Contrast  , FWhM et sensibilté magnétique et thermique 
######################################################################################


def CONTRAST(s,A1,theta,y0) :
    return theta *(   ( omega_R**2 ) /(  omega_R**2 + A1 * (s/(1+s))**2 )     ) +y0

def Width(s,A1,y0):
    return ((A1/sigmap)/(2*np.pi))*np.sqrt( (s/(1+s))**2     + (omega_R **2) /(A1)  ) +y0
                                                                        
def senmag(s,A1,theta,y0) :
    return P*( h/(g*mu) )*((( sigmac/(2*np.pi))*np.sqrt( (s/(1+s))**2     + omega_R**2 /(A1)  ))/ (  ( theta * (omega_R**2 /( omega_R**2 + A1 * (s/(1+s))**2 )  )   )*np.sqrt(R_sat*(s/ (1+s) )))) +y0 

def sentherm(s,A1,theta,y0):
    return P* (1/D)* ((( sigmac/(2*np.pi))*np.sqrt( (s/(1+s))**2     + omega_R**2 /(A1)  ))/ (  ( theta * (omega_R**2 /( omega_R**2 + A1 * (s/(1+s))**2 )  )   )*np.sqrt(R_sat*(s/ (1+s) )))) +y0



###################################################################
# parametres initiale pour le fitting
###################################################################
      #le contrast en Si (*2 pour %)
omega_R = 0.6*2*np.pi*10**6*np.sqrt(10**(10/10)) # relation between omega_R et la puissance en (dbm)
P = 0.77
R_sat =4493.67460234e3 # counts/s 
# R_sat =250e3
theta = 0.02   # (alpha-Beta/2 alpha)<0.5 
sigmap = 5e6    # rate of polarisation 
sigmac  = 8e7    # rate of coherence 
D = 71.2e3        # le chift de la resonance avec la temperature (K/Hz)
A1 = sigmac*sigmap

p01 = [A1,theta,0.6] #parametre initiale du fit prametrés par les parametres initiaux 
# p01 = [sigmap,sigmac,theta,-0.26]
# p02 = [sigmac,sigmap,-0.26e4]
# p02 = [5e5,8e9,-0.26e6]
p02 =[A1,-0.26e6]
# p03=[A1,-7e-10,theta]
p03= [A1,theta,0]
p04= [A1,theta,0]


C =-B1[:,1] # le Contrast de fitting ODMRS 

linwidth =(B1[:,2])*2



###########################################################################
# fitting
##########################################################################
LASER_power = np.ones(len(a))

for k in range(len(a)):
    LASER_power[k] = a[k] /493 # Various laser power 
Sfit =np.linspace ( LASER_power[0],LASER_power[16], 200 )



 

popt1, pcov1 = curve_fit(CONTRAST, LASER_power[:17]  ,C[:17] , p01)
fit1 = CONTRAST(Sfit, *popt1)
init1 = CONTRAST(Sfit, *p01)


popt2, pcov2 = curve_fit(Width, LASER_power[:17]  ,linwidth[:17] ,p02)
fit2 = Width(Sfit,*popt2)
init2 = Width(Sfit,*p02)



popt3, pcov3 = curve_fit(senmag, LASER_power[:17]  ,etha_mag[:17], p03)
fit3 = senmag(Sfit,*popt3)
init3= senmag(Sfit,*p03)




popt4, pcov4 = curve_fit(sentherm, LASER_power[:17]  ,etha[:17],p04)
fit4 = sentherm(Sfit,*popt4)
init4= sentherm(Sfit,*p04)

############################################################


Contrast_error = np.sqrt (B2[0:17,1])


plt.figure()
plt.xscale('log')
plt.plot(  LASER_power[:17]     ,   (C[:17])*1e2   ,'o' ,label='Experimental data'    )
plt.plot (  Sfit, (fit1)*1e2  ,'-'    ,label='Fitting data'                  )
plt.errorbar(LASER_power[:17], (C[:17])*1e2,  yerr = Contrast_error*1e2, fmt='|',ecolor = 'black',color='black',label='Error Bar')
#plt.ylim(min(fit1) ,5.2 )
# plt.xlim(0.24,2.1)
plt.ylabel("Contrast (%)")
plt.xlabel("S")
# plt.title("les paramÃ¨tres optimaux sont  ","A1 =",popt1(0),"theta =",popt1(1))
plt.legend()




linwidth_error = np.sqrt (B2[0:17,2])*2


plt.figure()
# plt.yscale('log')
plt.xscale('log')
plt.plot(  LASER_power[:17]     ,   linwidth[:17]   ,'o' ,label='Experimental data'    )
plt.plot(  Sfit, fit2 ,'-' ,label='Fitting data'     )
plt.errorbar(LASER_power[:17], linwidth[:17],  yerr=linwidth_error,fmt='|',ecolor = 'black',color='black',label='Error Bar')
plt.ylabel("FWHM (Hz) ")
plt.xlabel("S")
# plt.xlim(0.24,2.1)
# plt.title("A1 =",popt2(0))
# plt.ylim(min(fit2),max(fit2))
plt.legend()



# etha_mag_error = (etha_mag[:17])*1e6 * ( (linwidth_error/(B1[0:17,2]*2)) +   ((np.sqrt ((B2[0:17,1])))/-B1[0:17,1])   )
etha_mag_error = P*( h/(g*mu*C[:17]*np.sqrt(R_sat*(LASER_power[:17]/ (1+LASER_power[:17]) ))) )*( linwidth_error + linwidth[:17]  / C[:17]  * np.sqrt ((B2[0:17,1]))          )

plt.figure()
plt.xscale('log')
plt.plot(  LASER_power[:17] , (etha_mag[:17])*1e6  ,'o' ,label='Experimental data'    )
plt.plot (  Sfit,(fit3)*1e6,'-'    ,label='Fitting data' )
plt.errorbar(LASER_power[:17], (etha_mag[:17])*1e6 ,  yerr=(etha_mag_error)*1e6,fmt='|',ecolor = 'black',color='black',label='Error Bar')
# plt.xlim(0.18,2.1)
# plt.ylim(0,110)
plt.ylabel(' Magnetic sensitivity (\u03bcT/$\sqrt{Hz}$)')
plt.xlabel("S")
# plt.title("A1",popt3(0))
plt.legend()


# etha_therm_error = etha[:17] *((linwidth_error/(B1[0:17,2]*2)) +   ((np.sqrt ((B2[0:17,1])))/C[:17]) )  
etha_therm_error = P*   (1/(D*C[:17]*np.sqrt(R_sat*(LASER_power[:17]/ (1+LASER_power[:17]) ))) )*( linwidth_error + (linwidth[:17]  / C[:17])  * np.sqrt ((B2[0:17,1]))          )
plt.figure()
plt.xscale('log')
plt.plot(  LASER_power[:17] , etha[:17] ,'o' ,label='Experimental data'    )
plt.plot (  Sfit,fit4,'-'    ,label='Fitting data'                  )
plt.errorbar(LASER_power[:17], etha[:17],  yerr=etha_therm_error,fmt='|',ecolor = 'black',color='black',label='Error Bar')
plt.xlabel("S")
plt.ylabel('Thermal sensitivity (K/$\sqrt{Hz}$)')
# plt.title("A1",popt4(0))
plt.legend()
print ("popt1 =",popt1,"error1 =",np.sqrt(np.diag(pcov1)))
print ("popt2 =",popt2,"error2 =",np.sqrt(np.diag(pcov2)))
print( "popt3 =",popt3, "error3 =",np.sqrt(np.diag(pcov3)))
print( "popt4 =",popt4, "error4 =",np.sqrt(np.diag(pcov4)))