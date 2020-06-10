import numpy as np
import sys
##===============================
#
#   DECLARATIONS
#
##===============================

pi_inv = 1./np.pi

class lorentzian:
    def __init__(self, gamma, E0):
        self.gamma = gamma
        self.E0 = E0
        self.epsilon = 1e-4

        self.zero_interval = 2. * np.sqrt(self.gamma/(2.*np.pi*self.epsilon) - self.gamma**2/4.)

    def __call__(self, E):
        return 0.5 * self.gamma * pi_inv / ((E - self.E0)**2 + 0.25 * self.gamma**2)


    def get_zero_interval(self):
        return self.zero_interval