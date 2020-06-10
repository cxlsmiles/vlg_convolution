import sys

try:
    fname = sys.argv[1]
    shift = float(sys.argv[2])
    factor = float(sys.argv[3])
except IndexError:
    print('usage: %s [shift] [scaling factor]' % sys.argv[0])
    sys.exit(0)

with open(fname, 'r') as f:
    lns = f.readlines()

    ofile = open("sh."+fname, 'w')
    for i in range(len(lns)):
        en, int_ = lns[i].split()
        ofile.write("%10.5f  %20.6e\n" % (float(en)+shift, float(int_)*factor))
        print "%10.5f  %20.6e" % (float(en)+shift, float(int_)*factor)
    ofile.close()