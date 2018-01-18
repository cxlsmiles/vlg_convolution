import numpy as np
import sys
from lorentzian import *
##================================
#
#    MAIN :)
#
##================================

try:
   file = sys.argv[1]
   Gamma = float(sys.argv[2])
except IndexError:
   print "usage: %s [filename] [Gamma]" % sys.argv[0]
   sys.exit(1)


#Gamma = 0.112
Lor = Lorentzian(Gamma, 0.0)

#npts = 10000
#grid = np.linspace(-5.0, 5.0, npts)
#Lx = Lor(grid)
#
#for i in range(npts):
#    print "%15.10f  %15.10f" % (grid[i], Lx[i])


ifile = open(file, 'r')
lns = ifile.readlines()
ifile.close()

n = len(lns)
E = [float(lns[i].split()[0]) for i in range(n)]
f = [float(lns[i].split()[1]) for i in range(n)]


fg_conv = Convolve(f, Lor, E)


ofile = open("conv.%s" % file, 'w')
for i in range(len(E)):
    ofile.write("%10.6f  %20.10f\n" % (E[i], fg_conv[i]))
ofile.close()

