from datetime import date

#Perihelion: 22/5/1966


today = date.today()
d0 = date(1966, 5, 22)
d1 = date.today()
delta = d1 - d0 


import numpy as np

t = delta.days

p = 30685.4

e = 0.0457

o = 74.006

w = 96.998857

M = 360/(p) * (t) 

Ec = (180/(np.pi)) * ((2*(e)) * np.sin(np.pi/180 * M)) 

v = ((Ec)+(M)) + o + w

import matplotlib.pyplot as plt 

a = 19.19126
theta = v/180*np.pi
theta = np.linspace(0,2*np.pi, 360)
r = (a*(1-e**2))/(1+e*np.cos(theta))
plt.plot(theta, r, 'c')

r = (a*(1-(e*e)))/(1+e*np.cos(np.deg2rad(v)))

plt.plot(np.deg2rad(v),r,'go',markersize=5) 
