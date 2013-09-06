.PHONY: install clean clean-test test

install:
	echo "export PATH=$(shell pwd):$$PATH">>~/.bashrc
	echo "export PYTHONPATH=$(shell pwd)/lib:$$PYTHONPATH">>~/.bashrc
	./install.sh

test:
	./test.sh

help:
	@echo "make (install) - Add the PATH into ~/.bash_profile"
	@echo "make test - Test the genOpt"
	@echo "make clean - Delete all the pyc files in the ./lib"

clean: 
	-rm *.pyc
