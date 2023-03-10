import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum
from conservation_laws import Conservation

Pendulum1 = Conservation(1, 1, np.pi/16, 0, 0, 0, -9.81*1*(1-np.cos(np.pi/4)))



Pendulum3 = Conservation(1, 1, np.pi/16, 0, 0, 0, -9.81*1*(1-np.cos(np.pi/4)))


while Pendulum1.theta_0 >= 2*np.pi:
    Pendulum1.theta_0 = Pendulum1.theta_0 - 2*np.pi

while Pendulum3.theta_0 >= 2*np.pi:
    Pendulum3.theta_0 = Pendulum3.theta_0 - 2*np.pi
    
while Pendulum3.theta_0 <= 0:
    Pendulum3.theta_0 = Pendulum3.theta_0 + 2*np.pi

time1 = np.array(Pendulum1.time)
KE_1 = np.array(Pendulum1.kinetic_energy)
PE_1 = np.array(Pendulum1.potential_energy)



time3 = np.array(Pendulum3.time)
KE_3 = np.array(Pendulum3.kinetic_energy)
PE_3 = np.array(Pendulum3.potential_energy)

#time = []
#KE = []
#PE = []

for i in range(0, 20000):

    Pendulum1.update_angle(0.001)
    Pendulum1.energy()


    KE_1 = np.append(KE_1, Pendulum1.kinetic_energy)
    PE_1 = np.append(PE_1, Pendulum1.potential_energy)
    time1 = np.append(time1, Pendulum1.time)
    #time.append(Pendulum1.time)
    #KE.append(Pendulum1.kinetic_energy)
    #PE.append(Pendulum1.potential_energy)
    


    
    
    Pendulum3.runge_kutta(0.001)
    Pendulum3.energy()
    
    KE_3 = np.append(KE_3, Pendulum3.kinetic_energy)
    PE_3 = np.append(PE_3, Pendulum3.potential_energy)
    time3 = np.append(time3, Pendulum3.time)  
    

plt.plot(time1, KE_1, "r")
plt.plot(time1, PE_1, "b")
plt.plot(time1, KE_1+PE_1, "orange")
plt.show()


plt.plot(time3, KE_3, "r")
plt.plot(time3, PE_3, "b")
plt.plot(time3, KE_3+PE_3, "orange")
plt.show()

plt.plot(time1, KE_1+PE_1, "r", label = "Euler")
plt.plot(time3, KE_3+PE_3, "b", label = "RK")
plt.legend()
plt.xlim(0,20)
plt.ylim(-0.3, -0.1)
plt.show()



