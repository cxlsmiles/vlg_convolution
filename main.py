import numpy as np
import sys
from conv_discrete import *
import matplotlib.pyplot as plt

try:
   file = sys.argv[1]
   gamma = float(sys.argv[2])
   alpha = float(sys.argv[3])
   dx = float(sys.argv[4])
   npoints = int(sys.argv[5])
   tosave = sys.argv[6]
except IndexError:
   print "usage: %s [filename] [Gamma in EV!!!] [Alpha in EV] [dx] [npoints] [LVG]" % sys.argv[0]
   sys.exit(1)


ifile = open(file, 'r')
lns = ifile.readlines()
ifile.close()

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