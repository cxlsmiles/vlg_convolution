import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd

from conv_discrete import convolve
from conv_continuous import convolve_continuous
from find_duplicates import *
from gaussian import gaussian
from file_io import write_to_file

def main (fname, functionType, gamma, alpha, npoints, is_continuous):

    data = pd.read_csv(fname, header=None, delim_whitespace = True)
    data.columns = ["x", "fx"]

    if is_continuous:
        x = np.array(data.x)
        fx = np.array(data.fx)

        if len(functionType) == 1:
            convolutionOfFx = convolve_continuous(gamma, alpha, x, fx, functionType)

            write_to_file(fname, functionType, x, convolutionOfFx)
            
            plt.plot(x, fx, '-')
            plt.plot(x, convolutionOfFx, label=functionType)
        else:
            plt.plot(x, fx, '-', label='original spectrum')
            for i in range(len(functionType)):
                convolutionOfFx = convolve_continuous(gamma, alpha, x, fx, functionType[i])
                
                write_to_file(fname, functionType[i], x, convolutionOfFx)
                
                plt.plot(x, convolutionOfFx, label=functionType[i])
            plt.legend()
            plt.show()
        
    else:
        x, fx = remove_duplicates(data.x, data.fx)
        x, fx = remove_zero_intensity(x, fx)

        gauss_profile = gaussian(alpha, 0.0)
        interval = gauss_profile.get_zero_interval()
        xContinuous = np.linspace(x[0] - interval, x[-1] + interval, npoints)

        if len(functionType) == 1:
            convolutionOfFx = convolve(gamma, alpha, x, fx, xContinuous, functionType)
            write_to_file(fname, functionType, xContinuous, convolutionOfFx)

            plt.plot(x, fx, 'bo')
            plt.plot(xContinuous, convolutionOfFx, label=functionType)
        else:
            for i in range(len(functionType)):
                convolutionOfFx = convolve(gamma, alpha, x, fx, xContinuous, functionType[i])
                write_to_file(fname, functionType[i], xContinuous, convolutionOfFx)

                plt.plot(x, fx, 'bo')
                plt.plot(xContinuous, convolutionOfFx, label=functionType[i])
        plt.xlim([xContinuous[0], xContinuous[-1]])
        plt.legend()
        plt.show()

if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
        functionType = sys.argv[2]
        gamma = float(sys.argv[3])
        alpha = float(sys.argv[4])
        npoints = int(sys.argv[5])
        is_continuous = int(sys.argv[6])

    except IndexError:
        print("usage: %s [file name] [function type - G L V] [gamma] [alpha] [npoints] [is the spectrum continuous - T/F]\n" % sys.argv[0])
        sys.exit(0)

    main(fname, functionType, gamma, alpha, npoints, is_continuous)