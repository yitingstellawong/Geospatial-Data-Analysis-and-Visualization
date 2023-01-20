# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 15:31:42 2022

@author: ThinkBook
"""
import math
import numpy as np 
R, r, a = 6, 1, 8
x0, y0 = R+r-a, 0
nRev = 16

res = []
          
for t in np.arange(0, math.pi * nRev, 0.01):
    x = (R + r) * math.cos((r/R) * t)- a * math.cos((1 + r/R) * t)
    y = (R + r) * math.sin((r/R) * t) - a * math.sin((1 + r/R) * t)
    res.append((-118.285443 + 0.001 * x, 34.020559 + 0.001 * y))
    
with open("output.txt", 'w') as f:
    for i in res:
        f.write('{"loc": [' + str(i[0]) + "," + str(i[1]) + "]}," + '\n')


