import numpy as np
from gaussian import *
from lorentzian import *
import matplotlib.pyplot as plt

def my_conv(g_array, l_array):
        l_array = l_array[::-1]

        n = len(l_array)
        len_tot = 2*n - 1

        v_array = np.zeros(len_tot)

        for i in range(len_tot):
            if i + 1 > n:
                #print l_array[: len_tot - i]
                #print g_array[i-n+1:]
                v_array[i] = np.sum(g_array[i-n+1:] * l_array[: len_tot - i])
            else:
                #print l_array[-i-1:]
                #print g_array[:i+1]
                v_array[i] = np.sum(g_array[:i+1]*l_array[-i-1:])
        
        return v_array


def np_conv(g_array, l_array):
        v_array = np.convolve(g_array,l_array, 'same')*dx
        return v_array

x = np.linspace(-2.0,2.2,5)
dx = x[1]-x[0]

alpha, gamma = 1.0, 1.0
x0 = 0.1

gaus = gaussian(alpha,x0)
g_array = gaus(x)

lor = lorentzian(gamma,x0)
l_array = lor(x)


b = np.array([1,4,3,1])
a = np.array([1,1,5,5])
my_conv(a, b)

import sys
sys.exit(1)

v_array = np.zeros(len(x))

plt.plot(x, np_conv(g_array,l_array))
plt.plot(x, np_conv(g_array,l_array))
plt.plot(x, l_array)
plt.plot(x, g_array)
plt.show()py