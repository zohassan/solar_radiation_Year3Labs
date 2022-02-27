#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:18:27 2022

@author: Rohith
"""

from pysolar.solar import *
import datetime
import numpy as np
import matplotlib.pyplot as plt

time, intensity = np.loadtxt('SolarM_edit.csv', skiprows = 1, delimiter=',', unpack = True)

# %% SZA

from pysolar.solar import *
import datetime
import numpy as np

class SZA:
    

    
    def __init__(self,time):
        self.time = [int(a) for a in time]
        

    def hrmin(self):
        tdigits = []
        hour = []
        minu = []
        for i in range(len(self.time)):
            x = [int(a) for a in str(self.time[i])]
            tdigits.append(x)
            hr = tdigits[i][0]*10 + tdigits[i][1]
            mn = tdigits[i][2]*10 + tdigits[i][3]
            hour.append(hr)
            minu.append(mn)
        return hour,minu

    
    def Sza(self,lat,long,hour,minute):
        dobj = datetime.datetime(2022,2,25,hour,minute,tzinfo=datetime.timezone.utc)
        sza = float(90)- get_altitude(lat,long, dobj)
        cosZ = np.cos((sza/180)*np.pi)
        return 1/cosZ
    
    
    
    def secZ(self):
        secz = []
        for i in range(len(self.time)):
            Z = self.Sza(51.3,-0.07,self.hrmin()[0][i],self.hrmin()[1][i])
            secz.append(Z)
        return secz


# %% Optical Depth 

X = SZA(time)

class OpDepth:
    
    def __init__(self,secZ,intensity):
        self.secZ = secZ
        self.intensity = intensity 
         
    def pcov(self):
        fit, pcov = np.polyfit(self.secZ,np.log(self.intensity),1,cov = True)
        return pcov[0][0]
    
    def plot(self):   
        fit, pcov = np.polyfit(self.secZ,np.log(self.intensity),1,cov = True)
        sec_array = np.linspace(min(self.secZ),max(self.secZ),500)
        linearfit=np.poly1d(fit)  
        return plt.plot(sec_array,linearfit(sec_array)), plt.plot(self.secZ, np.log(self.intensity), 'x')
        
        
# %%


