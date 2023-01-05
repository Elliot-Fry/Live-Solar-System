from datetime import date

#Perihelion: 18/3/2011

today = date.today()
d0 = date(2011, 3, 18)
d1 = date.today()
delta = d1 - d0 

import numpy as np

t = delta.days

p = 4332.589

e = 0.0489

o = 100.464

w = 273.867

M = 360/(p) * (t) 

Ec = (180/(np.pi)) * ((2*(e)) * np.sin(np.pi/180 * M)) 

v = ((Ec)+(M)) + o + w

import matplotlib.pyplot as plt 

a = 5.20336
theta = v/180*np.pi
theta = np.linspace(0,2*np.pi, 360)
r = (a*(1-e**2))/(1+e*np.cos(theta))
plt.plot(theta, r, 'c')

r = (a*(1-(e*e)))/(1+e*np.cos(np.deg2rad(v)))
#gives distance to centre of planet from centre of sun, makes sure the point is on the orbital path

plt.plot(np.deg2rad(v),r,'ro',markersize=5) 
