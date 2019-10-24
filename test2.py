#!/usr/bin/python
# -*- coding: UTF-8 ;-*-
print('hello world')
for i in range(1,9,2):
    print(i)

import math

def Area (r):
    s=math.pi*r**2
    return s

r = 25
print(Area(r))
print(Area(10))