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

    def __call__(self, E):
         return 0.5 * self.gamma * pi_inv / ((E - self.E0)**2 + 0.25 * self.gamma**2)