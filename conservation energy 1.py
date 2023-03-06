import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum
from conservation_laws import Conservation

Pendulum1 = Conservation(1, 1, np.pi/4, 0, 0, 0, -9.81*1*(1-np.cos(np.pi/4)))



Pendulum3 = Conservation(1, 1, np.pi/4, 0, 0, 0, -9.81*1*(1-np.cos(np.pi/4)))


while Pendulum1.theta_0 >= 2*np.pi:
    Pendulum1.theta_0 = Pendulum1.theta_0 - 2*np.pi

while Pendulum3.theta_0 >= 2*np.pi:
    Pendulum3.theta_0 = Pendulum3.theta_0 - 2*np.pi
    
while Pendulum3.theta_0 <= 0:
    Pendulum3.theta_0 = Pendulum3.theta_0 + 2*np.pi

time = np.array(0)
KE_1 = np.array(0)
PE_1 = np.array(1-np.cos(np.pi/4))


KE_2 = np.array(0)
PE_2 = np.array(1-np.cos(np.pi/4))

KE_3 = np.array(0)
PE_3 = np.array(1-np.cos(np.pi/4))

#time = []
#KE = []
#PE = []

for i in range(0, 200):

    Pendulum1.update_angle(0.1)
    #print(Pendulum1.omega_0)
    #print(Pendulum1.kinetic_energy)
    Pendulum1.energy()


    KE_1 = np.append(KE_1, Pendulum1.kinetic_energy)
    PE_1 = np.append(PE_1, Pendulum1.potential_energy)
    #time.append(Pendulum1.time)
    #KE.append(Pendulum1.kinetic_energy)
    #PE.append(Pendulum1.potential_energy)
    


    
    
    Pendulum3.runge_kutta(0.1)
    Pendulum3.energy()
    
    KE_3 = np.append(KE_3, Pendulum3.kinetic_energy)
    PE_3 = np.append(PE_3, Pendulum3.potential_energy)
    
    
    time = np.append(time, i*0.1)
    
    

plt.plot(time, KE_1, "r")
plt.plot(time, PE_1, "b")
plt.plot(time, KE_1+PE_1, "orange")
plt.show()


#plt.plot(time, KE_2, "r")
#plt.plot(time, PE_2, "b")
#plt.plot(time, KE_2+PE_2, "orange")
#plt.show()

plt.plot(time, KE_3, "r")
plt.plot(time, PE_3, "b")
plt.plot(time, KE_3+PE_3, "orange")
plt.show()

