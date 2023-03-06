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
        
        
        #x = np.array(self.theta_0, self.omega_0)
        
        #x_dot = np.array(self.omega_0, -self.g/self.length * np.sin(self.theta_0))
        #theta_dot = self.omega_0
        omega_dot = -self.g/self.length * np.sin(self.theta_0)
        
        
        #k1 = x_dot * dt
        #k1_theta = theta_dot * dt
        k1_omega = omega_dot * dt
        
        #k2 = dt * np.array(x_dot[0] + k1[0]/2, x_dot[1] + k1[1]/2)
        #k2_theta = (theta_dot + k1_theta/2) * dt
        k2_omega = (omega_dot+ k1_omega/2) * dt      
                
        #k3 = dt * np.array(x_dot[0]+k2[0]/2, x_dot[1]+k2[1]/2)
        #k3_theta = (theta_dot + k2_theta/2) * dt
        k3_omega = (omega_dot + k2_omega/2) * dt        
        
        #k4 = dt * np.array(x_dot[0]+k3[0], x_dot[1]+k3[1])
        #k4_theta = (theta_dot + k3_theta) * dt
        k4_omega = (omega_dot + k3_omega) * dt      
        
        #x = x + 1/6 * (k1+ 2*k2 + 2*k3 +k4)
               
        
        
        #self.theta_0 = self.theta_0 + 1/6 * (k1_theta + 2*k2_theta + 2*k3_theta + k4_theta) * dt 
        
        self.omega_0 = self.omega_0 + 1/6 * (k1_omega + 2*k2_omega + 2*k3_omega + k4_omega)
        self.theta_0 = self.theta_0 + self.omega_0 * dt
        self.time = self.time + dt






