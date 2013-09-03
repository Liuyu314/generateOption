install:
	./setup.sh	
	echo "export PATH=~/.local/bin:$$PATH">>~/.bash_profile
	echo "export PYTHONPATH=~/.local/lib/python:$$PYTHONPATH">>~/.bash_profile
	source ~/.bash_profile

test:
	genOpt.py ./test/hello.c hello.scm hello.py

help:
	@echo " "

.PHONY: clean
clean: 
	-rm *.pyc
	-rm ./test/*

