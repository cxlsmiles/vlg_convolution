import numpy as np

class Gaussian:
    def __init__(self, fwhm, E0):
        self.alpha =  4 * np.log(2) / fwhm**2
        self.E0 = E0

    def __getitem__(self, E):
         return np.sqrt(self.alpha / np.pi) * np.exp( -(E - self.E0)**2 * self.alpha)

    def __call__(self, E):
         return np.sqrt(self.alpha / np.pi) * np.exp( -(E - self.E0)**2 * self.alpha)
