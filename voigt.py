import numpy as np
from gaussian import *
from lorentzian import *
import matplotlib.pyplot as plt
from conv_discrete import *
from scipy.special import wofz


class voigt:
    def __init__  (self, gamma, alpha, x0):
        self.gamma = gamma
        self.alpha = alpha
        self.x0 = x0


    def __call__(self, x_):
        gaus = gaussian(self.alpha,self.x0)
        g_array = gaus(x_)
    
        lor = lorentzian(self.gamma, 0.0)
        l_array = lor(x_)
        
        v_array = np.zeros(len(x_))
        dx = x_[1]-x_[0]

        for i in range(len(x_)):
            lor = lorentzian(self.gamma, x_[i])
            l_arr = lor(x_)
            
            prod = l_arr*g_array
            v_array[i] = np.trapz(prod, x = x_, dx=dx)
        
        return v_array

    def my_conv(self, x_):
        gaus = gaussian(self.alpha,self.x0)
        g_array = gaus(x_)
    
        lor = lorentzian(self.gamma, 0.0)
        l_array = lor(x_)
        
        v_array = np.zeros(len(x_))
        dx = x_[1]-x_[0]

        l_array = l_array[::-1]

        for i in range(len(l_array)):
            temp = 0.0
            for j in range(len(l_array)):
                temp += g_array[j]*l_array[i-j]
            v_array[i] = temp*dx
        return v_array

    def np_conv(self, x_):
        gaus = gaussian(self.alpha,self.x0)
        g_array = gaus(x_)
    
        lor = lorentzian(self.gamma, 0.0)
        l_array = lor(x_)
        
        v_array = np.zeros(len(x_))
        dx = x_[1]-x_[0]

        v_array = np.convolve(g_array,l_array, 'same')*dx

        return v_array

def V(x, alpha, gamma):
    """
    Return the Voigt line shape at x with Lorentzian component HWHM gamma
    and Gaussian component HWHM alpha.

    """
    sigma = alpha / np.sqrt(2 * np.log(2))

    return np.real(wofz((x + 1j*gamma)/sigma/np.sqrt(2))) / sigma /np.sqrt(2*np.pi)

def L(x, gamma):
    """ Return Lorentzian line shape at x with HWHM gamma """
    return gamma / np.pi / (x**2 + gamma**2)

if __name__ == "__main__":
    # x = np.linspace(2800,2840,1000)
    # v = voigt(0.3,0.64,5.0)
    # v2 = voigt(0.3,0.64,0.0)
    # v3 = voigt(0.3,0.64,2823.22933)
    # #plt.plot(x, v(x))    
    # plt.plot(x, v3(x))
    # plt.show()
    
    # print np.trapz(v3(x), x, dx=x[1]-x[0])

    # x1 = np.linspace(-10,10,1000)
    # plt.plot(x1,v2(x1))
    # plt.plot(x1,v(x1))
    # plt.show()


    alpha = 0.3/np.sqrt(2)
    gamma = 0.62/2
    
    # x2 = np.linspace(-10,10,1000)
    # v4 = voigt(0.8,0.64,0.0)
    # plt.plot(x2,v4(x2))
    # plt.plot(x2, v4.np_conv(x2))
    # plt.plot(x2, V(x2, alpha, gamma), c='k', label='Voigt')
    # plt.show()

    ifile = open("sh.xas.cl6w.6311ppg3df3pdnof.dat", 'r')
    lns = ifile.readlines()
    ifile.close()

    en = [float(lns[i].split()[0]) for i in range(len(lns))]
    int_ = [float(lns[i].split()[1]) for i in range(len(lns))]

    npts = 1000
    x = np.linspace(en[0]-10.0, en[-1]+10.0, npts)

    temp = np.zeros(npts)
    temp_l = np.zeros(npts)

    for i in range(len(en)):
        x_ = x - en[i]
        temp += V(x_, alpha, gamma)*int_[i]
        temp_l += L(x_, gamma)*int_[i]
        plt.plot(x, V(x_, alpha, gamma)*int_[i])
    
    ifile = open("conv.V.sh.xas.cl6w.6311ppg3df3pdnof.dat", 'r')
    lns = ifile.readlines()
    ifile.close()

    en1 = [float(lns[i].split()[0]) for i in range(len(lns))]
    int1 = [float(lns[i].split()[1]) for i in range(len(lns))]

    plt.vlines(en, 0, int_)
    plt.plot(x, temp)
    plt.plot(x, temp_l)
    plt.plot(en1, int1)
    plt.show()