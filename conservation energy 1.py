import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum
from conservation_laws import Conservation

Pendulum1 = Conservation(1, 1, np.pi/16, 0, 0, 0, -9.81*1*(1-np.cos(np.pi/16)))



Pendulum3 = Conservation(1, 1, np.pi/16, 0, 0, 0, -9.81*1*(1-np.cos(np.pi/16)))


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
    

plt.subplot(121)
plt.title("Euler Method")
plt.plot(time1, KE_1, "r", label="Kinetic Energy")
plt.plot(time1, PE_1, "b", label="Potential Energy")
plt.plot(time1, KE_1+PE_1, "orange", label="Total Energy")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.legend()



plt.subplot(122)
plt.title("Runge-Kutta Method")
plt.plot(time3, KE_3, "r", label="Kinetic Energy")
plt.plot(time3, PE_3, "b", label="Potential Energy")
plt.plot(time3, KE_3+PE_3, "orange", label="Total Energy")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.legend()
plt.show()

plt.plot(time1, KE_1+PE_1, "r", label = "Euler")
plt.plot(time3, KE_3+PE_3, "b", label = "RK")
plt.legend()
#plt.xlim(0,20)
#plt.ylim(-0.225, -0.150)
plt.xlabel("Time")
plt.ylabel("Energy")
plt.show()

total_1 = KE_1 + PE_1
total_2 = KE_3 + PE_3

change_1 = (total_1[1]-total_1[-1])/total_1[1]
change_2 = (total_2[1]-total_2[-1])/total_2[1]

print(change_1, change_2)




