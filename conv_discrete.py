import numpy as np
import sys
from lorentzian import *


try:
   file = sys.argv[1]
   Gamma = float(sys.argv[2])
   dx = float(sys.argv[3])
   npoints = int(sys.argv[4])
except IndexError:
   print "usage: %s [filename] [Gamma in EV!!!] [dx] [npoints]" % sys.argv[0]
   sys.exit(1)


ifile = open(file, 'r')
lns = ifile.readlines()
ifile.close()

n = len(lns)
E = [float(lns[i].split()[0]) for i in range(n)]
Int = [float(lns[i].split()[1]) for i in range(n)]

grid = np.linspace(E[0] - dx, E[-1] + dx, npoints)


Lors = []
for i in range(n):
    Li = Lorentzian(Gamma, E[i])
    Lors.append(Li(grid)*Int[i])


total = np.zeros(npoints)
for i in range(n):
    total = np.sum([total, Lors[i]], axis=0)

ofile = open('conv.%s' % file, 'w')
for i in range(npoints):
    ofile.write("%15.10f  %15.10f\n" % (grid[i], total[i]))
ofile.close()
   
