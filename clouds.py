# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:40:24 2022

@author: zoyaa
"""

import scipy as sp 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
import pandas as pd


folder_path = r"C:\Users\zoyaa\OneDrive\Documents\Year 3\Labs\Cyle 2"
file_name = r"\Trial log\data1.csv"
file_path = folder_path + file_name 
dF = pd.read_csv(file_path,sep='\t')


#sza_thermo = dF['SZA'][6:-2] 
#sza_light = dF['SZA'][14:-2]
#thermo = dF['Intensity (mV)'][6:-2] - sp.mean(dF['Intensity (mV)'][0:6])
#light = dF['Intensity (KfC'][14:-2]