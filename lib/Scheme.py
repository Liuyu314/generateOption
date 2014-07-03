#coding=utf-8

'''
This is a module for the type of Scheme language.
You should not run this code independently.
You can add some features for your own option.
'''

import os
import time
from func import *

class Scheme:
	
	def __init__(self):
		self.dict = readConfig()
	
	def addOption(self, f):
		f.write("; Author: %s" %self.dict['author'])
		f.write("; Email: %s" %self.dict['email'])
		f.write("; Time: %s\n" %self.dict['timeNow'])
		f.write("; Description:\n")
		f.write("; Version:\n")
		f.write("; Option:\n")
		f.write('\n')

if __name__ == "__main__":
	print "This is a module, you should not run it indepently!"
	print "Find the genOpt.py and run it! :)"