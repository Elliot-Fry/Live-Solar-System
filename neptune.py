from datetime import date

#Perihelion: 3/9/1876
#1876-Sep-03 

today = date.today()
d0 = date(1876, 9, 3)
d1 = date.today()
delta = d1 - d0 


import numpy as np

t = delta.days

p = 60189

e = 0.0113

o = 131.783

w = 273.187

M = 360/(p) * (t) 

Ec = (180/(np.pi)) * ((2*(e)) * np.sin(np.pi/180 * M)) 

v = ((Ec)+(M)) + o + w

import matplotlib.pyplot as plt 

a = 30.06896348
theta = v/180*np.pi
theta = np.linspace(0,2*np.pi, 360)
r = (a*(1-e**2))/(1+e*np.cos(theta))
plt.plot(theta, r, 'c')

r = (a*(1-(e*e)))/(1+e*np.cos(np.deg2rad(v)))

plt.plot(np.deg2rad(v),r,'bo',markersize=5) 
