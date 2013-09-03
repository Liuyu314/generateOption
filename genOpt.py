#! /usr/bin/python

import sys
import os

def openFile(f, lanType):
	if not os.path.exists(f):
		fp = open(f, 'w')
		obj = eval(lanType + '.' + lanType + '()')
		obj.addOption(fp)
		fp.close()
	else:
		fp = open(f, 'r')
		lines = fp.read()
		fp.close()
		fp = open(f, 'w')
		try:
			#obj = Python.Python()
			obj = eval(lanType + '.' + lanType + '()')
			obj.addOption(fp)
		finally:
			fp.write(lines)
			fp.close()

if len(sys.argv) == 1:
	print "Missing file"
else:
	if not os.path.exists("~/.local/bin/configTypes"):
		f = open("~/.local/bin/configTypes", 'w')
		f.write("#This is a config file which includes the accessable types\n")
		f.write("#input the types like this Python(py)\n")
		f.write("#remember to import Python\n")
		sys.exit()
	else:
		types_dic = {}
		types_f = open("~/.local/bin/configTypes", 'r')
		while True:
			inf_types = types_f.readline()
			#print inf_types,
			if len(inf_types) == 0:
				break
			if inf_types.startswith('#'):
				continue
			else:
				#count = 0
				#for i in inf_types:
				#	if i == '(':
				#		left = count
				#		value = inf_types[0:left]
				#	if i == ')':
				#		right = count
				#		key = inf_types[left + 1:right]
				#	count = count + 1
				value = inf_types.split('(')[0] #This two sentences can do the same thing with above code
				key = inf_types.split('(')[1].split(')')[0]
			types_dic[key] = value

		for module in types_dic:
			module_file = types_dic[module] + '.' + 'py'
			#print module_file 
			filepath = "~/.local/lib/python" + module_file
			if not os.path.exists(filepath):
				print "Error: %s is not exists in " %module_file,
				print filepath
				sys.exit()
			else:
				exec("import " + types_dic[module])
		#print types_dic
		types_f.close()

	for f in sys.argv[1:]:
		language_type = f.split('.')[1]
		if language_type in types_dic:
			openFile(f, types_dic[language_type])
			print "==============================================="
			print "Filetype of %s is" %f, types_dic[language_type]
			print "Option added"
			print "==============================================="
		else:
			print "%s is not a accessable file, please check the configTypes file" %f
			sys.exit()
