from gaussian import gaussian
from lorentzian import lorentzian
from voigt import voigt
import numpy as np


def convolve_continuous(alpha, gamma, x, fx, typeOfFunction):
   npoints = len(x)
   dx = x[1] - x[0]

   if typeOfFunction == 'G':
      gaussian_profile = gaussian(alpha, x[int(npoints/2)])
      gx = gaussian_profile(x)

   elif typeOfFunction == 'L':
      lorentzian_profile = lorentzian(gamma, x[int(npoints/2)])
      gx = lorentzian_profile(x)

   elif typeOfFunction == 'V':
      voigt_profile = voigt(gamma, alpha, x[int(npoints/2)])
      gx = voigt_profile(x)

   else:
      print('This type of function is not supported.\n')
      import sys
      sys.exit(0)

   assert(len(gx) == len(fx))
   
   return np.convolve(gx, fx, mode='same')*dx


if __name__ == "__main__":
   from scipy.special import wofz
   import matplotlib.pyplot as plt

   # def V(x, alpha, gamma):
   #    """
   #    Return the Voigt line shape at x with Lorentzian component HWHM gamma
   #    and Gaussian component HWHM alpha.

   #    """
   #    sigma = alpha / np.sqrt(2 * np.log(2))

   #    return np.real(wofz((x + 1j*gamma)/sigma/np.sqrt(2))) / sigma\
   #                                                          /np.sqrt(2*np.pi)


   # npoints = 10000
   # x = np.linspace(-10, 10, npoints)
   # alpha = 0.5
   # gamma = 0.5

   # vgt = V(x, alpha/2., gamma/2.)

   # conv_vgt = convolve_continuous(alpha, gamma, x, vgt, 'G')

   # plt.plot(x, vgt)
   # plt.plot(x, conv_vgt)
   # plt.show()
   
   with open('sum_Auger.dat', 'r') as f:
      lns = f.readlines()

      lns = lns[790:]
      x = []
      fx = []
      for i in range(len(lns)):
         x.append(float(lns[i].split()[0]))
         fx.append(float(lns[i].split()[1]))
      alpha = 0.5
      gamma = 1.0

      x = np.array(x)
      fx = np.array(fx)

      plt.plot(x, fx, label='unconvolved')
      for typeOfFunction in ['V', 'L', 'G']:
         fx_convolved = convolve_continuous(alpha, gamma, x, fx, typeOfFunction)
         plt.plot(x, fx_convolved, label=typeOfFunction)
      plt.legend()
      plt.show()