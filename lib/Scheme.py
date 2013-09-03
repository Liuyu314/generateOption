import os
import time

class Scheme:
	def __init__(self):
		if not os.path.exists("./config"):
			fp = open("./config", 'w')
			fp.write("Author:\n")
			fp.write("Email:\n")
			fp.close()
		else:
			fp = open("./config", 'r')
			while True:
				line = fp.readline()
				if len(line) == 0:
					break
				if line.startswith('Author'):
					Scheme.author = line.split(':')[1]
				if line.startswith('Email'):
					Scheme.email = line.split(':')[1]
				Scheme.timeNow = time.strftime('%Y,%m,%d %H:%M:%S')
			fp.close()

	def addOption(self, f):
		f.write("; Author: %s" %Scheme.author)
		f.write("; Email: %s" %Scheme.email)
		f.write("; Time: %s\n" %Scheme.timeNow)
		f.write("; Description:\n")
		f.write("; Version:\n")
		f.write("; Option:\n")
		f.write('\n')
