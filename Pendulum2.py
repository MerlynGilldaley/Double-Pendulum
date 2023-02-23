import numpy as np
import matplotlib.pyplot as plt
#import math



class Double_Pendulum():

    def __init__(self, mass1, mass2, length1, length2, theta1, theta2, omega1, omega2, g=9.81):
        
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.theta1 = theta1
        self.theta2 = theta2
        self.omega1 = omega1
        self.omega2 = omega2
        self.g = g

    def update_angle(self, dt):
        self.d_theta1 = self.omega1 * dt
        self.d_omega1 = (-self.g*(2*self.mass1+self.mass2)*np.sin(self.theta1)-self.mass2*self.g*np.sin(self.theta1+2*self.theta2)-2*np.sin(self.theta1-self.theta2)*self.mass2*(self.omega2**2*self.length2+self.omega1**2*self.length1*np.cos(self.theta1-self.theta2)))/(self.length1*(2*self.mass1+self.mass2-self.mass2*np.cos(2*self.theta1-2*self.theta2)))*dt
        self.d_theta2 = self.omega2 * dt
        self.d_omega2 = (2*np.sin(self.theta1-self.theta2)*(self.omega1**2*self.length1*(self.mass1+self.mass2)+self.g*(self.mass1+self.mass2)*np.cos(self.theta1)+self.omega2**2*self.length2*self.mass2*np.cos(self.theta1-self.theta2)))/(self.length2*(2*self.mass1+self.mass2-self.mass2*np.cos(2*self.theta1-2*self.theta2))) * dt
        self.time = (self.time*dt)


    


