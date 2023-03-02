import numpy as np
import matplotlib.pyplot as plt

from Pendulum1 import Pendulum

class Conservation(Pendulum):
    def __init__(self, length,mass, theta_0, omega_0, time, kinetic_energy, potential_energy, g=9.81):
        super().__init__(length,mass, theta_0, omega_0, time, g=-9.81)
        self.kinetic_energy = kinetic_energy
        self.potential_energy = potential_energy


    def energy(Pendulum, dt):

        
       #print(Pendulum.length)

       velocity_x = Pendulum.length * np.cos(Pendulum.theta_0)
       velocity_y = Pendulum.length * np.sin(Pendulum.theta_0)

       Conservation.kinetic_energy = (1/2) * Pendulum.mass * ((velocity_x)**2 + (velocity_y)**2)
       Conservation.potential_energy = Pendulum.mass * Pendulum.g * (Pendulum.length*(1-np.cos(Pendulum.theta_0)))


