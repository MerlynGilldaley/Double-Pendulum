# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:15:02 2023

@author: gilldale
"""

import numpy as np
from matplotlib import pyplot as plt


from Pendulum2 import Double_Pendulum
from Conservation_laws import Conservation

Pendulum = Conservation(1, 1, 1, 1, 0, np.pi/4, 0, 0, 0, 0, 19.61)

Pendulum2 = Conservation(1, 1, 1, 1, 0, np.pi/4, 0, 0, 0, 0, 19.61)



change_euler = np.array(0)
change_RK = np.array(0)
timestep = np.array(0)

for j in range(1, 100):

    dt =  j/1000
    
    #Time = np.array(Pendulum.time)
    KE = np.array(Pendulum.kinetic_energy)
    PE = np.array(Pendulum.potential_energy)

    #Time2 = np.array(Pendulum2.time)
    KE_2 = np.array(Pendulum2.kinetic_energy)
    PE_2 = np.array(Pendulum2.potential_energy)
    
    for i in range(0, 20000):
        
     
        #Uses the Conservation class and the RK4 method of integration to find the KE and PE
        #Appends these to the numpy arrays above
        Pendulum2.runge_kutta(dt)
        Pendulum2.energy()
        #Time2 = np.append(Time2, Pendulum2.time)
        KE_2 = np.append(KE_2, Pendulum2.kinetic_energy)
        PE_2 = np.append(PE_2, Pendulum2.potential_energy)

    

    Total_2 = np.array(KE_2 + PE_2)
    #print(Total, dt)

    Percent_change_2 = (Total_2[1] - Total_2[-1])/Total_2[1]
    

    change_RK = np.append(change_RK, Percent_change_2)
    timestep = np.append(timestep, dt)
    







plt.plot(timestep, change_RK, label="Runge-Kutta")
plt.legend()
plt.xlabel("Timestep")
plt.ylabel("Change in Energy")
plt.show()












