import numpy as np
import matplotlib.pyplot as plt
#import math

"""The Class "Double PEndulum" uses the imputs of the masses of the particles, the lengths of the strings and the initial angle of the 2 pendulums
   to define the motion of the double pendulum using the Euler method of integration"""

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

    