import numpy as np

from Pendulum2 import Double_Pendulum

"""Creates a subclass to ensure that the Double pendulum defined in Class(Double_Pendulum) obeys the conservation laws of energy and momentum"""

class Conservation(Double_Pendulum):

    def __init__(self, mass1, mass2, length1, length2, theta1, theta2, omega1, omega2, time, kinetic_energy, potential_energy, g=9.81):
        
        super().__init__(mass1, mass2, length1, length2, theta1, theta2, omega1, omega2, time, g=9.81)
        self.kinetic_energy = kinetic_energy
        self.potential_energy = potential_energy
        

    """Function to define the velocity of both masses in the pendulum in the x and y direction"""
    def energy(self):

        #self.kinetic_energy = 1/2 * (self.mass1+self.mass2)/2 * self.length1*self.length2 * (2*self.omega1**2 + self.omega2**2 + 2*self.omega1*self.omega2*np.cos(self.theta1 - self.theta2))
        #self.potential_energy = (self.mass1+self.mass2)/2 * self.g * (self.length1+self.length2)/2 * (3 - 2*np.cos(self.theta1) - np.cos(self.theta2))
        
        self.kinetic_energy = 1/2 * self.mass1*self.length1**2 * self.omega1**2 + 1/2 * self.mass2*self.length1**2 * self.omega1**2 + 1/2 * self.mass2 * self.length2**2 * self.omega2**2 + self.mass2*self.length1*self.length2*np.cos(self.theta1-self.theta2)*self.omega1*self.omega2
        self.potential_energy = self.mass1*self.g*self.length1*(1-np.cos(self.theta1))+self.mass2*self.g*(self.length1*(1-np.cos(self.theta1))+self.length1*(1-np.cos(self.theta2)))
        
        

        
        