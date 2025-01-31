# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:32:24 2023

@author: Cristian
problem number 34
number equal to the sum of the factorial of the individual digits
"""
import numpy as np

array = []
for x in range(145, 100000000):
    step1 = str(x)
    count = 0
    for y in range(len(step1)):
        count = np.math.factorial(int(step1[y])) + count
        #print(count)
    if count == x:
        array.append(x)
print(array)    
#This problem is solved