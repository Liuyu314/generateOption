import sys
import os

def addOption(f):
	f.write("hello\n")
	f.write("adsdasd\n")

def openFile(f):
	if not os.path.exists(f):
		fp = open(f, 'w')
		addOption(fp)
		fp.close()
	else:
		fp = open(f, 'r')
		lines = fp.read()
		fp.close()
		fp = open(f, 'w')
		addOption(fp)
		fp.write(lines)
		fp.close()

if len(sys.argv) == 0:
	print "Missing file"
else:
	for f in sys.argv[1:]:
		if f[-2:] == 'py':
			openFile(f)
			print "Option are already added in %s" %f
		else:
			print "%s is not a python file" %f
			sys.exit()
