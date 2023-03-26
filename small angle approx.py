# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:22:57 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum
#from Pendulum1 import update_angle

Pendulum1 = Pendulum(1,1, np.pi/4, 0, 0)

Pendulum2 = Pendulum(1,1, np.pi/4, 0, 0)

Pendulum3 = Pendulum(1,1, np.pi/4, 0, 0)

#Creating Arrays to save the data in:
time1=[0]
theta1=[Pendulum1.theta_0]
omega1=[Pendulum1.omega_0]

time2=[0]
theta2=[Pendulum2.theta_0]
omega2=[Pendulum2.omega_0]

time3=[0]
theta3=[Pendulum3.theta_0]
omega3=[Pendulum3.omega_0]

thetaT = [Pendulum3.theta_0]


#the number of iterations performed:
for j in range(1,7):
    
    theta = j/10
    
    for i in range (0,20000):
        
        
        
        
        
        
        Pendulum1.update_angle(0.001)
        
        
        
        
        time1.append(Pendulum1.time)
        theta1.append(Pendulum1.theta_0)
        omega1.append(Pendulum1.omega_0)
    
    
    
        
        
    
    
        Pendulum3.runge_kutta(0.001)
        
    
            
        #print(Pendulum3.theta_0) 
        
        time3.append(Pendulum3.time)
        theta3.append(Pendulum3.theta_0)
        omega3.append(Pendulum3.omega_0)    
        
        
        theta_T = np.pi/4 * np.cos(np.sqrt(9.81/1)*Pendulum3.time)
        thetaT.append(theta_T)

plt.plot(time1, theta1, "b")
plt.xlabel("Time (s)")
plt.ylabel("Angle (radians)")
#plt.xlim(0,20)
#plt.ylim(-0.1, 0.1)
plt.show()

#plt.plot(time2, theta2, "r")

plt.plot(time3, theta3, "orange")
plt.plot(time3, thetaT, label="Small angle approximation")


plt.xlabel("Time (s)")
plt.ylabel("Angle (radians)")
plt.xlim(0,20)
plt.show()


