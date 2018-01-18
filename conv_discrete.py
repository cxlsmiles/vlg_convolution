# Functions needed to go the convolution
import numpy as np
from lorentzian import *
from gaussian import *
from voigt import *


# Need to change this, this implementation is not very good

def convolve (gam, alph, x, fx, x_cont, np_, type):
    n = len(fx)

    funcs = []
    if type == "L":
        for i in range(n):
            fi = lorentzian(gam, x[i])
            funcs.append(fi(x_cont)*fx[i])
    elif type == "G":
        for i in range(n):
            fi = gaussian(alph, x[i])
            funcs.append(fi(x_cont)*fx[i])
    elif type == "V":
        for i in range(n):
            fi = voigt(gam, alph, x[i])
            funcs.append(fi(x_cont)*fx[i])


    sum_funcs = np.zeros(np_)
    for i in range(n):
         sum_funcs = np.sum([sum_funcs, funcs[i]], axis=0)   

    return sum_funcs