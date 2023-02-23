import numpy as np
import matplotlib.pyplot as plt
#import math



class Double_Pendulum():

    def __init__(self, mass1, mass2, length1, length2, theta1, theta2, omega1, omega2, time, g=-9.81):
        
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.theta1 = theta1
        self.theta2 = theta2
        self.omega1 = omega1
        self.omega2 = omega2
        self.time = time
        self.g = g

    """def update_angle(self, dt):
        self.d_theta1 = self.omega1 * dt
        self.d_omega1 = (-self.g*(2*self.mass1+self.mass2)*np.sin(self.theta1)-self.mass2*self.g*np.sin(self.theta1+2*self.theta2)-2*np.sin(self.theta1-self.theta2)*self.mass2*(self.omega2**2*self.length2+self.omega1**2*self.length1*np.cos(self.theta1-self.theta2)))/(self.length1*(2*self.mass1+self.mass2-self.mass2*np.cos(2*self.theta1-2*self.theta2)))*dt
        self.d_theta2 = self.omega2 * dt
        self.d_omega2 = (2*np.sin(self.theta1-self.theta2)*(self.omega1**2*self.length1*(self.mass1+self.mass2)+self.g*(self.mass1+self.mass2)*np.cos(self.theta1)+self.omega2**2*self.length2*self.mass2*np.cos(self.theta1-self.theta2)))/(self.length2*(2*self.mass1+self.mass2-self.mass2*np.cos(2*self.theta1-2*self.theta2))) * dt
        self.time = (self.time*dt)"""

    """Uses the Euler method of integration to update the angle and angular acceleration of both pendulums"""    
    def euler(self, dt):

        self.theta1 = self.theta1 + self.omega1 * dt
        self.omega1 = self.omega1 + (self.g/self.length1)*np.sin(self.theta1) * dt

        self.theta2 = self.theta2 + self.omega2 * dt
        self.omega2 = self.omega2 + (self.g/self.length2)*np.sin(self.theta2) * dt

        self.d_theta = self.theta1 - self.theta2
        self.omega1 -= (self.mass2/self.mass1)*(self.omega1 - self.omega2)*np.sin(self.d_theta)*dt
        self.omega2 -= (self.mass1/self.mass2)*(self.omega2 - self.omega1)*np.sin(self.d_theta)*dt

        self.time = self.time + dt

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def trapezoidal_rule(f, a, b, n):
        h = (b - a) / n
        sum = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            sum += f(a + i * h)
        return sum * h


