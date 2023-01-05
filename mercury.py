from datetime import date

today = date.today()

#Perihelia:
#20/10/2021
#15/1/2022
#13/4/2022

d0 = date(2021, 10, 20)
d1 = date.today()
delta = d1 - d0

import numpy as np

t = delta.days

p = 87.969 

e = 0.2056

o = 48.331

w = 29.124

M = 360/(p) * (t) 

Ec = (180/(np.pi)) * ((2*(e)) * np.sin(np.pi/180 * M)) 

v = ((Ec)+(M)) + o + w

import matplotlib.pyplot as plt 


a = 0.3871
theta = v/180*np.pi
theta = np.linspace(0,2*np.pi, 360)
r = (a*(1-e**2))/(1+e*np.cos(theta))
plt.plot(theta, r,'c')


r = (a*(1-(e*e)))/(1+e*np.cos(np.deg2rad(v)))
#gives distance to planet from centre of sun, makes sure the point is on the orbital path

plt.plot(np.deg2rad(v),r,'ko',markersize=5) 
