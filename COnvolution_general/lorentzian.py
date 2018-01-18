import numpy as np
##===============================
#
#   DECLARATIONS
#
##===============================

class Lorentzian:
    def __init__(self, gamma, E0):
        self.gamma = gamma
        self.E0 = E0

    def __getitem__(self, E):
         return 0.5 * self.gamma / ((E - self.E0)**2 + 0.25 * self.gamma**2)/np.pi

    def __call__(self, E):
         return 0.5 * self.gamma / ((E - self.E0)**2 + 0.25 * self.gamma**2)/np.pi
