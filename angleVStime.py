import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum
from Pendulum1 import update_angle

Pendulum1 = Pendulum(1, np.pi/4, 0, 0)

#Creating Arrays to save the data in:
time1=[0]
theta1=[Pendulum1.theta_0]
omega1=[Pendulum1.omega_0]


#the number of iterations performed:
for i in range (0,200):
    Pendulum1.update_angle(0.1)

    time1.append(Pendulum1.time)
    theta1.append(Pendulum1.theta_0)
    omega1.append(Pendulum1.omega_0)

plt.plot(time1, theta1)
plt.xlabel("Time (s)")
plt.ylabel("Angle (radians)")
plt.show()


Pendulum2 = update_angle(Pendulum1)

time2=[0]
theta2=[Pendulum2.theta_0]
omega2=[Pendulum2.omega_0]

for i in range(0, 200):
    Pendulum2.euler_cromer(0.1)

    time2.append(Pendulum1.time)
    theta2.append(Pendulum1.theta_0)
    omega2.append(Pendulum1.omega_0)

plt.plot(time2, theta2)
plt.show()