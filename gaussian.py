import numpy as np

pi_inv = 1.0/np.pi

sqrt_pi = np.sqrt(np.pi)
sqrt_pi_inv = 1.0/sqrt_pi

class gaussian:
    def __init__  (self, alpha, x0):
        self.alpha = alpha
        self.x0 = x0

    def __getitem__(self, x_):
        return np.sqrt(self.alpha) * sqrt_pi_inv * np.exp(- self.alpha * (x_ - self.x0)**2)

    def __call__(self, x_):
        return np.sqrt(self.alpha) * sqrt_pi_inv * np.exp(- self.alpha * (x_ - self.x0)**2)

    def at (self, x):
        x_ = np.array(x)
        return np.array(np.sqrt(self.alpha) * sqrt_pi_inv * np.exp(- self.alpha * (x_ - self.x0)**2))