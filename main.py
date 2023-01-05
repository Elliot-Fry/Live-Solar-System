#main.py is used to plot earth's orbit and the other orbits using import.
#0 degrees on the graph is the first point of ares (vernal equinox) 

#finding days since perihelion:
from datetime import date
today = date.today()
print("Today's date:", today) 

#Perihelion 2021 = 3/1 2021 
#Ph 2022 = 4/1 2022 
#Ph 2023 = 5/1 2023 

d0 = date(2021, 1, 3)
d1 = date.today()
delta = d1 - d0

#using eqation of centre to estimate true anomaly t sidereal days after perehelion:
#Ec = Equation of centre 
#v = True anomaly 
#M = Mean anomaly 
#e = orbital eccentricity 
#p = orbital period 
#t = sidereal days since perehelion 
#a = length of semimajor axis
#o = longditude of the ascending node 
#w = argument of perihelion 

import numpy as np

t = delta.days

p = 365.2564 

e = 0.0167 

o = (-11.26064)

w = 114.20783

M = 360/(p) * (t) 

Ec = (180/(np.pi)) * ((2*(e)) * np.sin(np.pi/180 * M)) 

v = ((Ec)+(M)) + o + w

#Plotting elliptical orbit: 

import matplotlib.pyplot as plt 
fig = plt.figure()
ax = fig.add_subplot(111, polar = True)

a = 1.00000011
theta = v/180*np.pi
theta = np.linspace(0,2*np.pi, 360)
r = (a*(1-e**2))/(1+e*np.cos(theta))
ax.plot(theta, r, 'c')

r = (a*(1-(e*e)))/(1+e*np.cos(np.deg2rad(v)))
#gives distance to centre of planet from centre of sun, makes sure the point is on the orbital path


print('Distance from sun to earth:', r,'AU') 


plt.plot(np.deg2rad(v),r,'bo',markersize=5) 
#plots the planet

plt.plot(0,0,'yo',markersize=5)
#plots the sun

import mercury, venus, mars, jupiter, saturn, uranus, neptune
#imports other planets and their orbits

plt.show()
