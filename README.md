# Live-Solar-System
A very simple python script applying basic orbital maths in order to generate a polar plot of the live positions of the planets in our solar system. With elliptical orbits and true anomalies. 

This code is based on the orbital maths outlined in Celestial Calculations: A Gentle Introduction to Computational Astronomy by J.L. Lawrence. 
The computation of the true anomalies (angular positions of planets in their orbital paths) is computed using the equation of the centre. 
This is an iterative function however for simplicity I truncated it afted one iteration. 
This means that true anomaly angles are only accurate to two or three significant figures. 
Accuracy can easily be improved by iterating the equation of the centre to as many iterations as needed. 
