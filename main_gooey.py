import numpy as np
import sys
from conv_discrete import *
import matplotlib.pyplot as plt
import sys
import argparse


from gooey import Gooey
from gooey import GooeyParser
@Gooey(program_name="Convolution of a discrete set of data")


def main():    
    parser = GooeyParser(description = "My cool app!")
    parser.add_argument('Filename', help = "file with stick spectrum", widget = 'FileChooser')
    parser.add_argument("Save", help = "the convolved function to be saved (LVG)")
    parser.add_argument("Gamma", help = "decay width in eV, parameter of the Lorentzian")
    parser.add_argument("Alpha", help = "gaussian broadening in eV, parameter of the Gaussian")
    parser.add_argument("Interval", help = "interval in x by which the grid for the convolution is extended")
    parser.add_argument("Npoints", help = "number of points of the grid of the convolution")
    
    args = parser.parse_args()


    ifile = open(args.Filename, 'r')
    lns = ifile.readlines()
    ifile.close()


    gamma = float(args.Gamma)
    alpha = float(args.Alpha)
    dx = float(args.Interval)
    npoints = int(args.Npoints)
    tosave = args.Save

    file = (args.Filename).split("\\")[-1]

    n = len(lns)
    e = [float(lns[i].split()[0]) for i in range(n)]
    f_e = [float(lns[i].split()[1]) for i in range(n)]

    grid = np.linspace(e[0] - dx, e[-1] + dx, npoints)

    tot_l = convolve(gamma, alpha, e, f_e, grid, npoints, "L")
    tot_v = convolve(gamma, alpha, e, f_e, grid, npoints, "V")
    tot_g = convolve(gamma, alpha, e, f_e, grid, npoints, "G")

    dict_lvg = {"L": tot_l,
                "G": tot_g,
                "V": tot_v}

    for s in range(len(tosave)):
        ofile = open('conv.%s.%s' % (tosave[s], file), 'w')

        arr = dict_lvg[tosave[s]]
        for i in range(npoints):
            ofile.write("%15.10f  %20.15e\n" % (grid[i], arr[i]))
        ofile.close()


    plt.plot(grid, tot_l)
    plt.plot(grid, tot_v)
    plt.plot(grid, tot_g)
    plt.show()

if __name__ == "__main__":
    sys.exit(main())