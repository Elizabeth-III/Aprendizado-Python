#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
