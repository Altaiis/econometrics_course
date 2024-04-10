#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:11:43 2020

@author: axelle
"""
# https://blog.rmhogervorst.nl/blog/2019/10/11/gosset-part-2-small-sample-statistics/#fn6

import pandas as pd
import numpy as np

np.random.seed(1)

mu, sigma = 133, 0.5 # mean and standard deviation

draws=1000   

d = {} 
for x in range(11):
    d["group" + str(x)] = np.random.normal(mu, sigma, size=(draws, x))

d_values = list(d.values())

# %% # 1 Draw
array1 = np.array(d_values[1])

array1.mean()
array1.mean(0)

array1[ np.where((array1 < (mu-sigma) ) |  (array1 > (mu+sigma) ) ) ]

freq1=( (array1 > (mu-sigma))  &  (array1 < (mu+sigma))).sum()
print(freq1/(1*draws))

array1.sum()/ (1*draws)

np.std(array1)
#/ N , where N = len(x)

# %% # 2 Draws
array2 = np.array(d_values[2])

array2.mean()
array2.mean(0)

array2[ np.where((array2 < 132 ) |  (array2 > (mu+sigma) ) ) ]
freq2=( (array2 > (mu-sigma))  &  (array2 < (mu+sigma))).sum()
print(freq2/(2*draws))

array2.sum()/ (2*draws)

np.std(array2)
# %% # 3 Draws
array3 = np.array(d_values[3])

array3.mean()
array3.mean(0)

array3[ np.where((array3 < (mu-sigma) ) |  (array3 > (mu+sigma) ) ) ]
freq3=( (array3 > (mu-sigma))  &  (array3 < (mu+sigma))).sum()
print(freq3/(3*draws))

array3.sum()/ (3*draws)

np.std(array3)

# %% # 4 Draws
array4 = np.array(d_values[4])

array4.mean()
array4.mean(0)

array4[ np.where((array4 < (mu-sigma) ) |  (array4 > (mu+sigma) ) ) ]
freq4=( (array4 > (mu-sigma))  &  (array4 < (mu+sigma))).sum()
print(freq4/(4*draws))

array4.sum()/ (4*draws)

np.std(array4)