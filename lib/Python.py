#coding=utf-8

'''
This is a module for the type of Python language.
You should not run this code independently.
You can add some features for your own option.
'''

import os
import time

if __name__ == "__main__":
	print "This is a module, you should not run it indepently!"
	print "Find the genOpt.py and run it! :)"
else:
	class Python:
		def __init__(self):
			fp = open("./config", 'r')
			while True:
				line = fp.readline()
				if len(line) == 0:
					break
				if line.startswith('#'):
					continue
				if line.startswith('Author'):	
					Python.author = line.split(':')[1]
				if line.startswith('Email'):
					Python.email = line.split(':')[1]
				Python.timeNow = time.strftime('%Y,%m,%d %H:%M:%S')
			fp.close()
	
		def addOption(self, f):
			f.write("'''\n")
			f.write("Author: %s" %Python.author)
			f.write("Email: %s" %Python.email)
			f.write("Time: %s\n" %Python.timeNow)
			f.write("Version: \n")
			f.write("Description:\n\n")
			f.write("'''\n")
			f.write('\n')
