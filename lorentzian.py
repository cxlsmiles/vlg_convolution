import numpy as np
import sys
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

def Convolve (f, g, xgrid):
    n = len(f)
    conv = np.zeros(n)
    dx = abs(xgrid[1] - xgrid[0])
    for i in range(n):
        temp = 0.0
        for j in range(n):
            temp += f[j] * g[xgrid[i] - xgrid[j]]
        conv[i] = temp * dx
    return conv

