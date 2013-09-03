import os
import time

class Python:
	def __init__(self):
		if not os.path.exists("config"):
			fp = open("config", 'w')
			fp.write("Author:\n")
			fp.write("Email:\n")
			fp.close()
		else:
			fp = open("config", 'r')
			while True:
				line = fp.readline()
				if len(line) == 0:
					break
				if line.startswith('Author'):
					Python.author = line.split(':')[1]
				if line.startswith('Email'):
					Python.email = line.split(':')[1]
				Python.timeNow = time.strftime('%Y,%m,%d %H:%M:%S')
			fp.close()

	def addOption(self, f):
		f.write("# Author: %s" %Python.author)
		f.write("# Email: %s" %Python.email)
		f.write("# Time: %s\n" %Python.timeNow)
		f.write("# Description:\n")
		f.write("# Version:\n")
		f.write("# Option:\n")
		f.write('\n')
