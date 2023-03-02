# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:21:21 2023

@author: gilldale
"""

import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum

Pendulum1 = Pendulum(1,1, np.pi/4, 0, 0, 0, 9.81*1*(1-np.cos(np.pi/4)))

while Pendulum1.theta_0 >= 2*np.pi:
    Pendulum1.theta_0 = Pendulum1.theta_0 - 2*np.pi

time = np.array(0)
KE = np.array(0)
PE = np.array(1-np.cos(np.pi/4))

for i in range(0, 200):
    Pendulum1.update_angle(0.1)
    
    print(Pendulum1.time)
    time = np.append(time, Pendulum1.time)
    print(Pendulum1.kinetic_energy)
    KE = np.append(KE, Pendulum1.kinetic_energy)
    print(Pendulum1.potential_energy)
    PE = np.append(PE, Pendulum1.potential_energy)
    
print(time)
print(KE)
print(PE)

    
plt.plot(time, KE)
plt.plot(time,PE)
plt.plot(time, KE+PE)
plt.show()