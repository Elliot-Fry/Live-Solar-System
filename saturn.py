from datetime import date

#Perihelion: 26/7/2003

today = date.today()
d0 = date(2003, 7, 29)
d1 = date.today()
delta = d1 - d0 


import numpy as np

t = delta.days

p = 10759.22

e = 0.0565

o = 113.665 

w = 	339.392

M = 360/(p) * (t) 

Ec = (180/(np.pi)) * ((2*(e)) * np.sin(np.pi/180 * M)) 

v = ((Ec)+(M)) + o + w

import matplotlib.pyplot as plt 

a = 9.53707
theta = v/180*np.pi
theta = np.linspace(0,2*np.pi, 360)
r = (a*(1-e**2))/(1+e*np.cos(theta))
plt.plot(theta, r, 'c')

r = (a*(1-(e*e)))/(1+e*np.cos(np.deg2rad(v)))
#gives distance to centre of planet from centre of sun, makes sure the point is on the orbital path

plt.plot(np.deg2rad(v),r,'yo',markersize=5) 

