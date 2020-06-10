import matplotlib.pyplot as plt

def write_to_file(fname, functionType, x, fx):
    with open("%s/conv.%s.%s" % (fname.split("/")[0], functionType, fname.split("/")[1]), 'w') as f:
        for i in range(len(x)):
            f.write("%f  %e\n" % (x[i], fx[i]))
    