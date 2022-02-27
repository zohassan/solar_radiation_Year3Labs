#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:35:31 2022

@author: Rohith
"""


import numpy as np
from szacalculator import SZA
from szacalculator import OpDepth
import matplotlib.pyplot as plt

Time, intensity = np.loadtxt('GFSolarM_edited.csv',skiprows = 1, delimiter=',', unpack = True)

# %%

A = SZA(Time)
secZ_gf = A.secZ()
lnI_gf = np.log(intensity)

B = OpDepth(A.secZ(), intensity)

B.plot()

print(B.pcov())

