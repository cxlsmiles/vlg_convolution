import numpy as np
from scipy.special import wofz
import pylab
from gaussian import gaussian
from lorentzian import lorentzian
from voigt import voigt


def G(x, alpha):
    """ Return Gaussian line shape at x with HWHM alpha """
    return np.sqrt(np.log(2) / np.pi) / alpha\
                             * np.exp(-(x / alpha)**2 * np.log(2))

def L(x, gamma):
    """ Return Lorentzian line shape at x with HWHM gamma """
    return gamma / np.pi / (x**2 + gamma**2)

def V(x, alpha, gamma):
    """
    Return the Voigt line shape at x with Lorentzian component HWHM gamma
    and Gaussian component HWHM alpha.

    """
    sigma = alpha / np.sqrt(2 * np.log(2))

    return np.real(wofz((x + 1j*gamma)/sigma/np.sqrt(2))) / sigma\
                                                           /np.sqrt(2*np.pi)

alpha, gamma = 0.1, 0.1


g_mine = gaussian(alpha*np.sqrt(2),0.0)
l_mine = lorentzian(gamma*2.0, 0.0)
v_mine = voigt(alpha*np.sqrt(2),gamma*2.0, 0.0)
x = np.linspace(-0.8,0.8,1000)
pylab.plot(x, G(x, alpha), ls=':', c='k', label='Gaussian')
pylab.plot(x, g_mine(x))
pylab.plot(x, L(x, gamma), ls='--', c='k', label='Lorentzian')
pylab.plot(x, l_mine(x))
pylab.plot(x, V(x, alpha, gamma), c='k', label='Voigt')
pylab.plot(x, v_mine(x))
pylab.plot(x, v_mine.np_conv(x))
pylab.xlim(-0.8,0.8)
pylab.legend()
pylab.show()