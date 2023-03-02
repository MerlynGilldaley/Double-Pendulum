import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum
from conservation_laws import Conservation

Pendulum1 = Conservation(1,1, np.pi/4, 0, 0, 0, 9.81*1*(1-np.cos(np.pi/4)))

while Pendulum1.theta_0 >= 2*np.pi:
    Pendulum1.theta_0 = Pendulum1.theta_0 - 2*np.pi

time = np.array(0)
KE = np.array(0)
PE = np.array(1-np.cos(np.pi/4))

for i in range(0, 200):

    Pendulum1.energy(0.1)

    np.append(time, i*0.1)
    #print(time)
    print(i*0.1)
    np.append(KE, Pendulum1.kinetic_energy)
    #print(KE)
    print(Pendulum1.kinetic_energy)
    np.append(PE, Pendulum1.potential_energy)
    #print(PE)
    print(Pendulum1.potential_energy)


print(time)
print(KE)
print(PE)

plt.plot(time, KE)
plt.plot(time, PE)
plt.plot(time, KE+PE)
plt.show()

