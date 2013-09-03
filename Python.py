import time

class Python:
	def addAuthor(self, f, author):
		f.write("# Author: %s\n" %author)
	def addEmail(self, f, email):
		f.write("# Email: %s\n" %email)
	def addTime(self, f, time):
		time = time.strftime('%Y, %m, %d, %H:%M:%S')
		f.write("# Time: %s" %time)
	def addOther(self, f):
		f.write("# Description:")
		f.write("# Version:")
		f.write("# Option::")
