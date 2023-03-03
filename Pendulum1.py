import numpy as np
import matplotlib.pyplot as plt


"""A class to define a single pendulum. Variables need: length, initial theta, angular acceleration, Time, deltaT and g."""

class Pendulum():
    def __init__(self, length, mass, theta_0, omega_0, time, g=-9.81):
        self.length = length
        self.mass = mass
        self.theta_0 = theta_0
        self.omega_0 = omega_0
        self.time = time
        self.g = g
               

    """Simulates the motion of the pendulum using Euler's method of integration
       Variables: length, initial theta, initial angular acceleration, time, deltaT"""

    def update_angle(self, dt):       
        
        self.omega_0 = (self.omega_0 - (self.g/self.length) * np.sin(self.theta_0) *dt)
        self.theta_0 = (self.theta_0 + self.omega_0 * dt)
        self.time = (self.time + dt)






