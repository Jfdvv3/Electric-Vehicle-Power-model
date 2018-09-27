# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:55:14 2018

@author: jay
"""

import math
import matplotlib.pyplot as plt

Vc = 27.8
alpha = 0.0
Rhoair = 1.2
Cdrag = 0.306
A = 2.38
Cfric = 0.02
g = 9.8
a = 5.0

Frr = Cfric * Mc * g * math.cos(alpha)

Fad = 0.5 * Rhoair * Cdrag * A * Vc ** 2

Frg = Mc * g * math.sin(alpha)

Fa = Mc * a

Frl = Frr + Fad + Frg + Fa

Pmax = Frl * Vc

Pavg = (Frl - Fa)*Vc

Vliion = 4.1
liionamphr = 2.4
Crateliion = 1
Iliion = liionamphr*Crateliion
SE = 200
Mbcalc = []

Acell = math.pi*(0.009**2)*0.0065
nn = []
MM = []
Abatt1 = []
Preq = []
for i in range(500):
    Mov = float(2320 - 417 + i)
    MM.append(i)
    n = ((Vc)/(Vliion*Iliion))*(Fad+Mov*(Cfric*g*math.cos(alpha)+a))
    nn.append(n)
    Abatt1.append(Acell*n)
    Wh = liionamphr*Vliion*n
    Mcalc = Wh/SE
    Mbcalc.append(Mcalc)
    Pcalc = Vc * Fad*Mov*(Cfric * g * math.cos(alpha)+g*math.sin(alpha)+a)
    Preq.append(Pcalc)
Ten = 10
Iliion10 = liionamphr*Ten
Tenn = []

Abatt10 = []
Mbcalc10 = []
for q in range(500):
    Mov = float(2320 - 417 + q)
    n = ((Vc)/(Vliion*Iliion10))*(Fad+Mov*(Cfric*g*math.cos(alpha)+a))
    Tenn.append(n)
    Abatt10.append(Acell*n)
    Wh = liionamphr*Vliion*n
    Mcalc = Wh/SE
    Mbcalc10.append(Mcalc)

Abonnet = 0.82*0.82*0.68
print Abonnet
ZZ = []
for i in range(500):
    ZZ.append(Abonnet)
""" PLOTS for LiCo"""
plt.figure(1)
OneC = plt.plot(MM, nn)
plt.plot(Mbcalc, nn)
plt.title("Mass of LiCo Battery vs. Number of 18650 cells for Pmax 1C")
plt.ylabel("Number of 18650 batteries")
plt.xlabel("mass of the battery (kg)")

plt.figure(2)
TenC = plt.plot(MM, Tenn)
plt.plot(Mbcalc10, Tenn)
plt.title("Mass of LiCo Battery vs. Number of 18650 cells  for Pmax 10C")
plt.ylabel("Number of 18650 batteries")
plt.xlabel("mass of the battery (kg)")

plt.figure(4)
plt.plot(MM, Abatt10)
# plt.plot(MM, ZZ)
plt.title("Volume of battery vs. mass of battery (10C LiCo)")
plt.ylabel("Volume of 18650 cells m^2")
plt.xlabel("mass of the battery (kg)")

plt.figure(3)
test = plt.plot(MM, Abatt1)
# plt.plot(MM, ZZ)
plt.title("Volume of battery vs. mass of battery (1C LiCo)")
plt.ylabel("Volume of 18650 cells m^2")
plt.xlabel("mass of the battery (kg)")

"""LiM Calculations"""
Vlim = 3.5
limamphr = 1.1
Cratelim = 10
Ilim = limamphr*Cratelim

Nlimcells = []
Mlim = []
Mlimcalc = []
Vbattlim = []
for i in range(500):
    Mov = float(2320 - 417 + i)
    Mlim.append(i)
    n = ((Vc)/(Vlim*Ilim))*(Fad+Mov*(Cfric*g*math.cos(alpha)+a))
    Nlimcells.append(n)
    Vbattlim.append(Acell*n)
    Wh = limamphr*Vlim*n
    Mcalc = Wh/SE
    Mlimcalc.append(Mcalc)

""" PLOTS FOR LiM """
plt.figure(5)
plt.plot(Mlim, Nlimcells)
plt.plot(Mlimcalc, Nlimcells)
plt.title("Mass of Battery vs. Number of 18650 cells required for Pmax 10C")
plt.ylabel("Number of 18650 batteries")
plt.xlabel("mass of the battery (kg)")

plt.figure(6)
plt.plot(Mlim, Vbattlim)
# plt.plot(MM, ZZ)
plt.title("Volume of battery vs. mass of battery (10C LiM)")
plt.ylabel("Volume of 18650 cells m^2")
plt.xlabel("mass of the battery (kg)")

plt.figure(7)
plt.plot(MM, Preq)
plt.title("Mass of battery vs Power required for peak conditions")
plt.ylabel("Power required W")
plt.xlabel("mass of the battery (kg)")
"""
Vnmc = 3.7
nmcAH = 2
Cratenmc = 10
Inmc = nmcAH * Cratenmc

Nnmccells = Pmax/(Vnmc*Inmc)"""
