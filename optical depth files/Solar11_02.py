#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:44:18 2022

@author: Rohith
"""

import numpy as np
from szacalculator import SZA
from szacalculator import OpDepth
from szacalculator import Trans
import matplotlib.pyplot as plt 

# %% 11/02

Time, intensity = np.loadtxt('SolarM11.csv',skiprows = 1, delimiter=',', unpack = True)

A = SZA(Time,11)
B = OpDepth(A.secZ(),intensity)

B.plot()
print(B.pcov())

#%% 25/02


Time, intensity = np.loadtxt('SolarM_10-11.csv',skiprows = 1, delimiter=',', unpack = True)

A = SZA(Time,11)
B = OpDepth(A.secZ(),intensity)

B.plot()
print(B.pcov())
