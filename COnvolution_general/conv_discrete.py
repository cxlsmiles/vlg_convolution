import numpy as np
import sys
from lorentzian import *
from gaussian import *
from convolve import *


try:
   file = sys.argv[1]
   type = sys.argv[2]
   Gamma = float(sys.argv[3])
   dx = float(sys.argv[4])
   npoints = int(sys.argv[5])
except IndexError:
   print "usage: %s [filename] [funcion_type - G/L] [Gamma in EV!!!] [dx] [npoints]" % sys.argv[0]
   sys.exit(1)


ifile = open(file, 'r')
lns = ifile.readlines()
ifile.close()

n = len(lns)
E = [float(lns[i].split()[0]) for i in range(n)]
Int = [float(lns[i].split()[1]) for i in range(n)]

grid = np.linspace(E[0] - dx, E[-1] + dx, npoints)

func_types = {"G": Gaussian, "L": Lorentzian}

Conv_Lines = []
for i in range(n):
    Conv_func = func_types[type](Gamma, E[i])
    Conv_Lines.append(Conv_func(grid)*Int[i])


total = np.zeros(npoints)
for i in range(n):
    total = np.sum([total, Conv_Lines[i]], axis=0)

total *= abs(grid[1]-grid[0])

ofile = open('conv.%s.%s' % (type,file), 'w')
for i in range(npoints):
    ofile.write("%15.10f  %15.10f\n" % (grid[i], total[i]))
ofile.close()
   
