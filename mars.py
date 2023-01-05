from datetime import date

#Perihelion: 3/8/2020

today = date.today()
d0 = date(2020, 8, 3)
d1 = date.today()
delta = d1 - d0 

import numpy as np

p = 686.980

t = delta.days

e = 0.0935

o = 49.558

w = 286.502

M = 360/(p) * (t) 

Ec = (180/(np.pi)) * ((2*(e)) * np.sin(np.deg2rad(M))) 

v = ((Ec)+(M)) + o + w

import matplotlib.pyplot as plt 

a = 1.52357
theta = v/180*np.pi
theta = np.linspace(0,2*np.pi, 360)
r = (a*(1-e**2))/(1+e*np.cos(theta))
plt.plot(theta, r, 'c')

r = (a*(1-(e*e)))/(1+e*np.cos(np.deg2rad(v)))
#gives distance to centre of planet from centre of sun, makes sure the point is on the orbital path

plt.plot(np.deg2rad(v),r,'ro',markersize=5) 
