import numpy as np

def Convolve (f, g, xgrid):
    n = len(f)
    conv = np.zeros(n)
    dx = abs(xgrid[1] - xgrid[0])
    for i in range(n):
        temp = 0.0
        for j in range(n):
            temp += f[j] * g[xgrid[i] - xgrid[j]]
        conv[i] = temp * dx
    return conv
