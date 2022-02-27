#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 21:18:04 2022

@author: Rohith
"""

import numpy as np
from szacalculator import SZA
from szacalculator import OpDepth

Time, intensity = np.loadtxt('Lightmeter_edited.csv',skiprows = 1, delimiter=',', unpack = True)

C = SZA(Time)
secZ_gf = C.secZ()
lnI_gf = np.log(intensity)

D = OpDepth(C.secZ(), intensity)

D.plot()

print(D.pcov())
