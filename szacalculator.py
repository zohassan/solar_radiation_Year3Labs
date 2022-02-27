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

time, intensity = np.loadtxt('SolarM.csv', skiprows = 1, delimiter=',', unpack = True)

# %% SZA
time = [int(a) for a in time]

def hrmin(time):
    tdigits = []
    hour = []
    minu = []
    for i in range(len(time)):
        x = [int(a) for a in str(time[i])]
        tdigits.append(x)
        hr = tdigits[i][0]*10 + tdigits[i][1]
        mn = tdigits[i][2]*10 + tdigits[i][3]
        hour.append(hr)
        minu.append(mn)
    return hour,minu

    
hour, minute = hrmin(time)

def Sza(lat,long,hour,minute):
    dobj = datetime.datetime(2022,2,25,hour,minute,tzinfo=datetime.timezone.utc)
    sza = float(90)- get_altitude(lat,long, dobj)
    cosZ = np.cos((sza/180)*np.pi)
    return 1/cosZ

secZ = []

for i in range(len(time)):
    Z = Sza(51.3,-0.07,hour[i],minute[i])
    secZ.append(Z)


# %% Optical Depth 

lnI = np.log(intensity)
plt.plot(secZ[0:31], lnI[0:31], 'x')

# %%

min_fake = np.linspace(0,58,30)
min_fake = [int(a) for a in min_fake]
fake_secZ = []

for i in range(len(min_fake)):
    Z = Sza(51.3,-0.07,15,min_fake[i])
    fake_secZ.append(Z) 

plt.plot(min_fake,fake_secZ)
