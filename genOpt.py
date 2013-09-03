import sys
import os
#import Python

def addOption(f):
	f.write("test\n")

def openFile(f):
	if not os.path.exists(f):
		fp = open(f, 'w')
		#addOption(fp)
		obj = Python.Python()
		obj.addAuthor(fp, "liuyu")
		fp.close()
	else:
		fp = open(f, 'r')
		lines = fp.read()
		fp.close()
		fp = open(f, 'w')
		#addOption(fp)
		obj = Python.Python()
		obj.addAuthor(fp, "liuyu")
		fp.write(lines)
		fp.close()


if len(sys.argv) == 1:
	print "Missing file"
else:
	if not os.path.exists("configTypes"):
		f = open("configTypes", 'w')
		f.write("#This is a config file which includes the accessable types\n")
		f.write("#input the types like this Python(py)\n")
		f.write("#remember to import Python\n")
		sys.exit()
	else:
		types_dic = {}
		types_f = open("configTypes", 'r')
		while True:
			inf_types = types_f.readline()
			#print inf_types,
			if len(inf_types) == 0:
				break
			if inf_types.startswith('#'):
				continue
			else:
				count = 0
				for i in inf_types:
					if i == '(':
						left = count
						value = inf_types[0:left]
					if i == ')':
						right = count
						key = inf_types[left + 1:right]
					count = count + 1
			types_dic[key] = value
		for module in types_dic:
			module_file = types_dic[module] + '.' + 'py'
			#print module_file 
			if not os.path.exists(module_file):
				print "Error: %s is not exists!" %module_file
				sys.exit()
			else:
				__import__(types_dic[module])
		#print types_dic
		types_f.close()

	for f in sys.argv[1:]:
		language_type = f[f.rfind('.') + 1:]
		#print language_type
		if language_type in types_dic:
			openFile(f)
			print "Filetype of %s is" %f, types_dic[language_type]
			print "Option added"
		else:
			print "%s is not a accessable file, please check the configTypes file" %f
			sys.exit()
