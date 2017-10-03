# -*- coding: utf-8 -*-
#!/bin/env/python
"""
Created on Thu Sep 28 15:33:30 2017

@author: jub061
"""
import sys
import numpy as np
import math

import scipy 
from scipy import stats as stat
import random as rand

inputs = [0.763, 0.720, 0.751, 0.743]
mean = np.mean(inputs)
std = np.std(inputs)
err = stat.sem(inputs)
var = np.var(inputs)
dof = len(inputs) - 1



trials = 10000
rang_set = 0.99

x_ = []
for i in range(0,trials):
    y = mean + stat.t.ppf(rand.random(), dof) * (math.pow(-1, math.ceil(rand.random()*2))) * err + stat.t.ppf(rand.random(), dof) * (math.pow(-1, math.ceil(rand.random()*2))) * math.sqrt(dof) * (var / (stat.chi.ppf(rand.random(), dof)))
    
    if i%100 == 0:
        print(i)    
    
    x_.append(y)
    
    x = sorted(x_)
print (x)

rang_95_high = math.floor(trials*0.95)
rang_95_low = math.floor(trials*(1-.95))
rang_set_high = math.floor(trials*rang_set)
rang_set_low = math.floor(trials*(1-rang_set))

rang_95_high_val = x[rang_95_high-1]
rang_95_low_val = x[rang_95_low-1]
rang_set_high_val = x[rang_set_high-1]
rang_set_low_val = x[rang_set_low-1]

print('The 95% range is ', rang_95_high_val, 'to ', rang_95_low_val)
print('The',rang_set*100, '% range is ', rang_set_high_val, 'to ', rang_set_low_val)

