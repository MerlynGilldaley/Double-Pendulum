import numpy as np
import matplotlib.pyplot as plt

from Pendulum2 import Double_Pendulum

Pendulum = Double_Pendulum(1, 1, 1, 1, np.pi/4, np.pi/4, 0, 0, 0)

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
print(Theta1)
print(Theta2)


plt.plot(Time, Theta1, "b")
plt.plot(Time, Theta2, "r")
plt.show()


x1 = Pendulum.length1 * np.sin(Theta1)
y1 = -Pendulum.length1 * np.cos(Theta1)
x2 = x1 + Pendulum.length2 * np.sin(Theta2)
y2 = y1 - Pendulum.length2 * np.cos(Theta2)
plt.plot(x1, y1, "b")
plt.plot(x2, y2, "r")
plt.show()


