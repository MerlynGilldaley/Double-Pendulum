import numpy as np
from matplotlib import pyplot as plt


from Pendulum2 import Double_Pendulum
from Conservation_laws import Conservation

Pendulum = Conservation(1, 1, 1, 1, np.pi/4, np.pi/4, 0, 0, 0, 0, 0)

while Pendulum.theta1 >= 2*np.pi:
    Pendulum.theta1 = Pendulum.theta1 - 2*np.pi

    #Why does this stop working at theta1 > 25*pi???
        
while Pendulum.theta2 >= 2*np.pi:
    Pendulum.theta2 = Pendulum.theta2 - 2*np.pi

    #Why does this stop working at theta2 > 13*pi???

Time = np.array(Pendulum.time)
Theta1=np.array(Pendulum.theta1)
Omega1=np.array(Pendulum.omega1)
Theta2=np.array(Pendulum.theta2)
Omega2=np.array(Pendulum.omega2)

KE = np.array(Pendulum.kinetic_energy)
PE = np.array(Pendulum.potential_energy)

 
for i in range(0, 200):
    Pendulum.euler(0.1)

    
    Time = np.append(Time, Pendulum.time)
    Theta1 = np.append(Theta1, Pendulum.theta1)
    Omega1 = np.append(Omega1, Pendulum.omega1)
    Theta2 = np.append(Theta2, Pendulum.theta2)
    Omega2 = np.append(Omega2, Pendulum.omega2)

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

