import numpy as np
from lorentzian import *
from gaussian import *
from voigt import *
import matplotlib.pyplot as plt


def convolve (gamma, alpha, x, fx, xContinuous, typeOfFunction):
    lenFx = len(fx)

    functionValues = []
    if typeOfFunction == "L":
        for i in range(lenFx):
            lorentzian_profile = lorentzian(gamma, x[i])
            functionValues.append(lorentzian_profile(xContinuous)*fx[i])

    elif typeOfFunction == "G":
        for i in range(lenFx):
            gaussian_profile = gaussian(alpha, x[i])
            functionValues.append(gaussian_profile(xContinuous)*fx[i])

    elif typeOfFunction == "V":
        for i in range(lenFx):
            voigt_profile = voigt(gamma, alpha, x[i])
            functionValues.append(voigt_profile(xContinuous)*fx[i])

    sumOfConvolutions = np.sum(functionValues, axis=0)

    return sumOfConvolutions