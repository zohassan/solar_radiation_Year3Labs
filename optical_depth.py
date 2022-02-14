# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:04:32 2022

Graphing and Plotting : Some Boiler code as well 


"""
import scipy as sp 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
import pandas as pd


folder_path = r"C:\Users\zoyaa\OneDrive\Documents\Year 3\Labs\Cyle 2"
file_name = r"\Clear_Sky\07Feb_lightandthermo.csv"
file_path = folder_path + file_name 
dF = pd.read_csv(file_path)


sza_thermo = dF['SZA'][6:-2] 
sza_light = dF['SZA'][14:-2]
thermo = dF['Intensity (mV)'][6:-2] - sp.mean(dF['Intensity (mV)'][0:6])
light = dF['Intensity (KfC'][14:-2]

#This needs to be changed 


intensity = light
sza = sza_light
Ierr = 0.01


plt.plot(1/sza,sp.log(intensity),'x',color='blue',mew = 2,ms=12,label ='Lightmeter Intensities')
plt.errorbar(1/sza,sp.log(intensity),yerr=Ierr/sp.log(intensity),fmt='x',color='blue')

fit,pcov = sp.polyfit(1/sza,sp.log(intensity),1,cov=True)

sec_array = sp.linspace(2.4950,2.505,100)
linearfit=sp.poly1d(fit)
plt.plot(sec_array,linearfit(sec_array),color='red',lw=2,label = 'Natural log fit')

plt.xlabel('sec(Z)',fontsize = 33)
plt.ylabel('Natural Log of Intensity, mV',fontsize = 33)
plt.legend(fontsize = 32)
plt.title('Clear Sky',fontsize = 33)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.figsize'] = (20,10)
plt.grid(True)
plt.tick_params(axis = 'both',labelsize = 28)
#plt.savefig('07Feb_clearsky_lightmeter.png',bbox_inches='tight')
plt.show()