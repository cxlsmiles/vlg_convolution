import sys

ifile = open(sys.argv[1], 'r')
lns = ifile.readlines()
ifile.close()

shift = float(sys.argv[2])
factor = float(sys.argv[3])


ofile = open("sh."+sys.argv[1], 'w')
for i in range(len(lns)):
    en, int_ = lns[i].split()
    ofile.write("%10.5f  %20.6e\n" % (float(en)+shift, float(int_)*factor))
    print "%10.5f  %20.6e" % (float(en)+shift, float(int_)*factor)
ofile.close()