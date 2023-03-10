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
        
        

        
    
    def runge_kutta(self, dt):
        
        def theta_dot(omega_0):
            return omega_0
        def omega_dot(theta_0):
            return -(self.g/self.length)*np.sin(theta_0)
        
        
        
        k1 = theta_dot(self.omega_0) #* dt
        m1 = omega_dot(self.theta_0) #* dt
        
        k2 = theta_dot(self.omega_0 + 1/2 * m1 * dt)
        m2 = omega_dot(self.theta_0 + 1/2 * k1 * dt)
        
        k3 = theta_dot(self.omega_0 + 1/2 * m2 * dt)
        m3 = omega_dot(self.theta_0 + 1/2 * k2 * dt)
        
        k4 = theta_dot(self.omega_0 + m3 * dt)
        m4 = omega_dot(self.theta_0 + k3 * dt)

        
        
        self.theta_0 = self.theta_0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4) * dt
        self.omega_0 = self.omega_0 + 1/6 * (m1 + 2*m2 + 2*m3 + m4) * dt
        self.time = self.time+dt





