from datetime import date

#Perihelion: 12/6/2021

today = date.today()
d0 = date(2021, 6, 12)
d1 = date.today()
delta = d1 - d0 

import numpy as np

t = delta.days

p = 224.701

e = 0.0067

o = 76.680 

w = 54.884

M = 360/(p) * (t) 

Ec = (180/(np.pi)) * ((2*(e)) * np.sin(np.pi/180 * M)) 

v = ((Ec)+(M)) + o + w

import matplotlib.pyplot as plt 

a = 0.72333
theta = v/180*np.pi
theta = np.linspace(0,2*np.pi, 360)
r = (a*(1-e**2))/(1+e*np.cos(theta))
plt.plot(theta, r, 'c')

r = (a*(1-(e*e)))/(1+e*np.cos(np.deg2rad(v)))
#gives diharea to planet from centre of sun, makes sure the point is on the orbital path

plt.plot(np.deg2rad(v),r,'mo',markersize=5) 

