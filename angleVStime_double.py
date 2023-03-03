import numpy as np
import matplotlib.pyplot as plt

from Pendulum2 import Double_Pendulum

"""The class Double_Pendulum:
    mass1, mass2, length1, length2, theta1, theta2, omega1, omega2, initial time
    It then uses the Euler method of numerical integration to update the angles and angular accelerations
    Both angles are then plotted against time and the x and y coordinates are calculated and plotted"""

Pendulum = Double_Pendulum(1, 1, 1, 2, np.pi/4, np.pi/4, 0, 0, 0)

while Pendulum.theta1 >= 2*np.pi:
    Pendulum.theta1 = Pendulum.theta1 - 2*np.pi

    #Why does this stop working at theta1 > 25*pi???
        
while Pendulum.theta2 >= 2*np.pi:
    Pendulum.theta2 = Pendulum.theta2 - 2*np.pi

    #Why does this stop working at theta2 > 13*pi???

Time = [Pendulum.time]
Theta1=[Pendulum.theta1]
Omega1=[Pendulum.omega1]
Theta2=[Pendulum.theta2]
Omega2=[Pendulum.omega2]


for i in range(0, 200):
    Pendulum.euler(0.1)

    
    Time.append(Pendulum.time)
    Theta1.append(Pendulum.theta1)
    Omega1.append(Pendulum.omega1)
    Theta2.append(Pendulum.theta2)
    Omega2.append(Pendulum.omega2)

#print(Time)
#print(Theta1)
#print(Theta2)


x1 = Pendulum.length1 * np.sin(Theta1)
y1 = -Pendulum.length1 * np.cos(Theta1)
x2 = x1 + Pendulum.length2 * np.sin(Theta2)
y2 = y1 - Pendulum.length2 * np.cos(Theta2)

plt.subplot(121)
plt.plot(Time, Theta1, "b")
plt.plot(Time, Theta2, "r")
plt.xlabel("Time / s")
plt.ylabel("Angle / rad")
#plt.show()

plt.subplot(122)
plt.plot(x1, y1, "b")
plt.plot(x2, y2, "r")
plt.xlabel("x-coordinates")
plt.ylabel("y-coordinates")
plt.tight_layout()
plt.show()


