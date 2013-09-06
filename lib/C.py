#coding=utf-8

'''
This is a module for the type of C language.
You should not run this code independently.
You can add some features for your own option.
'''

import os
import time

if __name__ == "__main__":
	print "This is a module, you should not run it indepently!"
	print "Find the genOpt.py and run it! :)"
else:
	class C:
		def __init__(self):
			fp = open("./config", 'r')
			while True:
				line = fp.readline()
				if len(line) == 0:
					break
				if line.startswith('#'):
					continue
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
