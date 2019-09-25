import numpy as np
from numpy import sin, cos, pi
from scipy.integrate import quad
from scipy.constants import pi, hbar
import matplotlib.pyplot as plt


"""
This python file is simply compiled to calculate
infinite well problems, it may not be thorough though.
"""

well_width = input("well width: ")
N = input("Least order of bases: ")
m = input("Mass of particle: ")

# The orthonormal bases of the system to nth order
def base():
    a = well_width
    base_list = []
    for state in range(1,N+1):
        base_list.append(lambda x: np.sqrt(2/a) * sin(state*pi/a*x) )
    return base_list

# Set the initial wave-function in code: Phi.function
class Phi():
    def __init__(self):
        self.a = well_width

    def function(self,x,t):
        def form(x):
            if x > self.a/2:
                K = x
            else:
                K = self.a-x
            return K
        def integrand(x):
            return form(x)**2
        self.coefficient = quad(integrand,0,self.a)[0]
        return form(x) / self.coefficient

def energy(n):
    return (hbar*pi*n)**2 / (2*m*well_width**2)
def freq(n):
    return hbar*(pi*n)**2 / (2*m*well_width**2)

def propagator(t,n):
    return np.exp(-1j * freq(n) * t)

if __name__ == "__main__":
    pass
