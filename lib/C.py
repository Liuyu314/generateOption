import os
import time

class C:
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
					C.author = line.split(':')[1]
				if line.startswith('Email'):
					C.email = line.split(':')[1]
				C.timeNow = time.strftime('%Y,%m,%d %H:%M:%S')
			fp.close()

	def addOption(self, f):
		f.write("/****************************************************\n")
		f.write(" *    Author: %s" %C.author)
		f.write(" *    Email: %s" %C.email)
		f.write(" *    Time: %s\n" %C.timeNow)
		f.write(" *    Description:\n")
		f.write(" *    Version:\n")
		f.write(" *    Option:\n")
		f.write("****************************************************/\n")
		f.write('\n')
