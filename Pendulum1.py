import numpy as np
import matplotlib.pyplot as plt


"""A class to define a single pendulum. Variables need: length, initial theta, angular acceleration, Time, deltaT and g."""

class Pendulum():
    def __init__(self, length, mass, theta_0, omega_0, time, kinetic_energy, potential_energy, g=9.81):
        self.length = length
        self.mass = mass
        self.theta_0 = theta_0
        self.omega_0 = omega_0
        self.time = time
        self.kinetic_energy = kinetic_energy
        self.potential_energy = potential_energy
        self.g = g
               

    """Simulates the motion of the pendulum using Euler's method of integration
       Variables: length, initial theta, initial angular acceleration, time, deltaT"""

    def update_angle(self, dt):       
        
        self.omega_0 = (self.omega_0 - (self.g/self.length) * np.sin(self.theta_0) *dt)
        self.theta_0 = (self.theta_0 + self.omega_0 * dt)
        self.time = (self.time + dt)
        
        velocity_x = self.length * np.cos(self.theta_0)
        velocity_y = self.length * np.sin(self.theta_0)

        self.kinetic_energy = (1/2) * self.mass * ((velocity_x)**2 + (velocity_y)**2)
        self.potential_energy = self.mass * self.g * (self.length*(1-np.cos(self.theta_0)))
        







