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
        
        
        

    
    def runge_kutta(self, theta1, omega1, theta2, omega2, dt):
        
        def omegadot_1(theta1, theta2):
        #calculates the angular acceleration of the first pendulum
            
            num = -self.g * (2*self.mass1+self.mass2)*np.sin(theta1)-self.mass2*self.g*np.sin(theta1-2*theta2)-2*self.mass2*np.sin(theta1-theta2) * (self.length2*(omega2)**2+self.length1*(omega1)**2 * np.cos(theta1-theta2))
            den = self.length1 * (2*self.mass1+self.mass2-self.mass2 * np.cos(2*theta1 - 2* theta2))
            return num/den
        
        def omegadot_2(theta1, theta2):
        #calculates the angular acceleration of the second pendulum
            
            temp = (2*np.sin(theta1 - theta2))
            num = temp * (self.length1 * (omega1)**2 * (self.mass1+self.mass2)+self.g*(self.mass1+self.mass2)*np.cos(theta1)+self.length2*(omega2)**2 * self.mass2*np.cos(theta1-theta2))            
            den = self.length2 * (2*self.mass1+self.mass2-self.mass2*np.cos(2*theta1 - 2*theta2))
            return num/den
        
        def thetadot_1(omega1):
            return omega1
        
        def thetadot_2(omega2):
            return omega2
        
        k1_1 = thetadot_1(self.omega1)
        k1_2 = thetadot_2(self.omega2)
        
        m1_1 = omegadot_1(self.theta1, self.theta2)
        m1_2 = omegadot_2(self.theta1, self.theta2)   
        
        
        k2_1 = thetadot_1(self.omega1 + m1_1 * (1/2) * dt)
        k2_2 = thetadot_2(self.omega2 + m1_2 * (1/2) * dt)
        
        m2_1 = omegadot_1(self.theta1 + k1_1/2 * dt, self.theta2 + k1_1/2 * dt)
        m2_2 = omegadot_2(self.theta1 + k1_2/2 * dt, self.theta2 + k1_2/2 * dt)
        
        
        k3_1 = thetadot_1(self.omega1 + m2_1/2 * dt)
        k3_2 = thetadot_2(self.omega2 + m2_2/2 * dt)
        
        m3_1 = omegadot_1(self.theta1 + k2_1/2 * dt, self.theta2 + k2_1/2 * dt)
        m3_2 = omegadot_2(self.theta1 + k2_2/2 * dt, self.theta2 + k2_2/2 * dt)
        
        
        k4_1 = thetadot_1(self.omega1 + m3_1 * dt)
        k4_2 = thetadot_2(self.omega2 + m3_2 * dt)
        
        m4_1 = omegadot_1(self.theta1 +k3_1 * dt, self.theta2 + k3_1 * dt)
        m4_2 = omegadot_2(self.theta1 + k3_2 * dt, self.theta2 + k3_2 * dt)
        
        
        
        self.theta1 = self.theta1 + 1/6 * (k1_1 + 2*k2_1 + 2*k3_1 + k4_1) * dt
        self.theta2 = self.theta2 + 1/6 * (k1_2 + 2*k2_2 + 2*k3_2 + k4_2) * dt
        
        self.omega1 = self.omega1 + 1/6 * (m1_1 + 2*m2_1 + 2*m3_1 + m4_1) * dt
        self.omega2 = self.omega2 + 1/6 * (m2_1 + 2*m2_2 + 2*m3_2 + m4_2) * dt
        
        self.time = self.time + dt
        
        
        
        
        
        
    
    
            
        

        

        
        
        
        
        
        
        
        
        
        
        

    