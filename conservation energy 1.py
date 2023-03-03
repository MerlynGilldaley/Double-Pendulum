import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum
from conservation_laws import Conservation

Pendulum1 = Conservation(1, 1, np.pi/4, 0, 0, 0, -9.81*1*(1-np.cos(np.pi/4)))

while Pendulum1.theta_0 >= 2*np.pi:
    Pendulum1.theta_0 = Pendulum1.theta_0 - 2*np.pi

time = np.array(0)
KE = np.array(0)
PE = np.array(1-np.cos(np.pi/4))

#time = []
#KE = []
#PE = []

for i in range(0, 200):

    Pendulum1.update_angle(0.1)
    #print(Pendulum1.omega_0)
    #print(Pendulum1.kinetic_energy)
    Pendulum1.energy()

    time = np.append(time, i*0.1)
    KE = np.append(KE, Pendulum1.kinetic_energy)
    PE = np.append(PE, Pendulum1.potential_energy)
    #time.append(Pendulum1.time)
    #KE.append(Pendulum1.kinetic_energy)
    #PE.append(Pendulum1.potential_energy)
    
    
    
    
print(time)
print(KE)
print(PE)

plt.plot(time, KE, "r")
plt.plot(time, PE, "b")
plt.plot(time, KE+PE, "orange")
plt.show()

