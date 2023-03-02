import numpy as np
import matplotlib.pyplot as plt

def simulate_pendulum(l, theta_0, omega_0, T, dt):
    g=9.8
    theta = [theta_0]
    omega = [omega_0]
    t = [0]
    while t[-1] < T:
        omega.append(omega[-1] - (g/l) * np.sin(theta[-1]) * dt)
        theta.append(theta[-1] + omega[-1] * dt)
        t.append(t[-1] + dt)
    return np.array(theta), np.array(omega), np.array(t)

theta, omega, t = simulate_pendulum(1, np.pi/4, 0, 10, 0.01)
plt.plot(t, theta)
plt.xlabel("Time (s)")
plt.ylabel("Angle (radians)")
plt.show()
