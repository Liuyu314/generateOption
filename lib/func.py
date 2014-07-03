#coding=utf-8

import os
import time

def readConfig():

	config_dict = {}
	fp = open("./config", 'r')

	while True:
		line = fp.readline()
		if len(line) == 0:
			break
		if line.startswith('#'):
			continue
		if line.startswith('Author'):
			config_dict['author'] = line.split(':')[1]
		if line.startswith('Email'):
			config_dict['email'] = line.split(':')[1]
		config_dict['timeNow'] = time.strftime('%Y,%m,%d %H:%M:%S')

	fp.close()

	return config_dict	
	

if __name__ == "__main__":
	print "This is a module, you should not run it indepently!"
	print "Find the genOpt.py and run it! :)"
