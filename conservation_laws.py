import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum

class Conservation(Pendulum):
    def __init__(self, length, mass, theta_0, omega_0, time, kinetic_energy, potential_energy, g=-9.81):
        super().__init__(length, mass, theta_0, omega_0, time, g=-9.81)
        self.kinetic_energy = kinetic_energy
        self.potential_energy = potential_energy


    def energy(self):

        
        #Pendulum.update_angle(0.1)

        velocity = self.length * self.omega_0
        
        

        
        self.kinetic_energy = (1/2) * self.mass * velocity**2
        #print(self.omega_0)
        self.potential_energy = self.mass * self.g * (self.length*(1-np.cos(self.theta_0)))
        #print(Conservation.kinetic_energy)
        
