import numpy as np
from gaussian import *
from lorentzian import *
import matplotlib.pyplot as plt
from scipy.special import voigt_profile


class voigt:
    def __init__  (self, gamma, alpha, x0):
        self.gamma = gamma
        self.alpha = alpha
        self.x0 = x0


        # Source wiki: https://en.wikipedia.org/wiki/Voigt_profile
        self.fg = self.alpha*np.sqrt(np.log(2))
        self.fl = self.gamma
        self.fv = 0.5346*self.fl + np.sqrt(0.2166*self.fl**2 + self.fg**2)

        self.zero_interval = 8.*self.fv

    def __call__(self, x):
        sigma = self.alpha / (2. * np.sqrt(2. * np.log(2.)))
        gamma = self.gamma/2.
        return voigt_profile((np.array(x) - self.x0), sigma, gamma)

    def _np_conv(self, x):
        # This class member function is used only for testing
        gaussian_profile = gaussian(self.alpha,self.x0)
        gx = gaussian_profile(x)
    
        lorentzian_profile = lorentzian(self.gamma, 0.0)
        lx = lorentzian_profile(x)
        
        dx = x[1]-x[0]

        return np.convolve(gx,lx, 'same')*dx

    def get_zero_interval (self):
        return self.zero_interval

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

    import numpy as np
    alpha = 0.3/np.sqrt(2)
    #gamma = 0.62/2
    gamma = 0.62

    fg = alpha*np.sqrt(np.log(2))
    fl = gamma

    fv = 0.5346*fl + np.sqrt(0.2166*fl**2 + fg**2)

    x = np.linspace(-5, 5, 1000)
    v_instance = voigt(gamma, alpha, 0.0)
    varr = v_instance(x)


    # print(6.*fv)
    # tmparr = np.where(x > 7.*fv)
    # index = tmparr[0][0]
    # print(index)
    # print(varr[index])

    import matplotlib.pyplot as plt

    plt.plot(x, varr, label='fv = %5.2f' % (fv))
    plt.plot(x, V(x, alpha, gamma))
    plt.legend()
    plt.show()

    import sys; sys.exit(1)
    
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