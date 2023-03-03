import numpy as np
from matplotlib import pyplot as plt


from Pendulum2 import Double_Pendulum
from Conservation_laws import Conservation

Pendulum = Conservation(1, 1, 1, 1, np.pi/4, np.pi/4, 0, 0, 0, 0, 19.61)

while Pendulum.theta1 >= 2*np.pi:
    Pendulum.theta1 = Pendulum.theta1 - 2*np.pi

    #Why does this stop working at theta1 > 25*pi???
        
while Pendulum.theta2 >= 2*np.pi:
    Pendulum.theta2 = Pendulum.theta2 - 2*np.pi

    #Why does this stop working at theta2 > 13*pi???

Time = np.array(Pendulum.time)

KE = np.array(Pendulum.kinetic_energy)
PE = np.array(Pendulum.potential_energy)

 
for i in range(0, 200):
    Pendulum.euler(0.1)

    
    Time = np.append(Time, Pendulum.time)


    Pendulum.energy()

    KE = np.append(KE, Pendulum.kinetic_energy)
    PE = np.append(PE, Pendulum.potential_energy)

#print(KE)
#print(PE)

#print(Time)

total = KE + PE

plt.plot(Time, KE, label="KE")
plt.plot(Time, PE, label="PE")
plt.plot(Time, total, label="total")
plt.legend()
plt.show()

