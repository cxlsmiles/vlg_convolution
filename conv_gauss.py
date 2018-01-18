import numpy as np
import sys

try:
   file = sys.argv[1]
except IndexError:
   print "usage: %s [filename]" % sys.argv[0]
   sys.exit(1)

class Gaussian:
    def __init__(self, alpha):
        self.alpha = alpha

    def __getitem__(self, x):
         return np.sqrt(self.alpha / np.pi) * np.exp( -x*x * self.alpha)

#f = Gaussian(2.0)
#FWHM = 0.94
sigma = 0.0849
FWHM = 2*sigma*np.sqrt(2*np.log(2))
alpha = 4 * np.log(2) / FWHM**2
print alpha
print 0.5/(sigma**2)
g = Gaussian(alpha)

#fg = Gaussian(2.0/3.0)

def Convolve (f, g, xgrid):
    n = len(xgrid)
    sum = np.zeros(n)
    
    dx = xgrid[1] - xgrid[0]
    for i in range(n):
        xi = xgrid[i]
        temp = 0.0
        for j in range(n):
            xj = xgrid[j]
            temp += f[j] * g[xi - xj] * dx
        sum[i] = temp
    return sum

ifile = open(file, 'r')
lns = ifile.readlines()
ifile.close()

n = len(lns)
x = [float(lns[i].split()[0]) for i in range(n)]
f = [float(lns[i].split()[1]) for i in range(n)]


fg_conv = Convolve(f, g, x)
print len(fg_conv)
print len(x)

#fg = np.sqrt(np.pi/3.0)*fg[x]

ofile = open("conv.%s" % file, 'w')
for i in range(len(x)):
    ofile.write("%5.3f  %20.10f\n" % (x[i], fg_conv[i])) #, fg[i]))
ofile.close()

