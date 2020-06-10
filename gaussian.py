import numpy as np

pi_inv = 1.0/np.pi

sqrt_pi = np.sqrt(np.pi)
sqrt_pi_inv = 1.0/sqrt_pi
sqrt_pi_ = np.sqrt(2*np.log(2)/np.pi)

class gaussian:
    def __init__  (self, alpha, x0):
        # alpha is FWHM
        # alpha related to sigma (the variance) as: alpha = 2*sqrt(ln 2) * sigma
        self.alpha = alpha
        self.x0 = x0
        self.epsilon = 1e-15

        self.zero_interval = 2. * self.alpha * np.sqrt(-2. * np.log(self.epsilon))

    def __call__(self, x_):
        return 1.0/self.alpha * sqrt_pi_ * np.exp(- 2*np.log(2)* (x_ - self.x0)**2/(self.alpha**2))


    def get_zero_interval (self):
        return self.zero_interval