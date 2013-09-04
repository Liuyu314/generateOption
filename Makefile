.PHONY: install clean clean-test test

install:
	echo "export PATH=~/generateOption:$$PATH">>~/.bash_profile
	echo "export PYTHONPATH=~/generateOption/lib:$$PYTHONPATH">>~/.bash_profile
	source ~/.bash_profile

test:
	./test.sh

help:
	@echo "make (install) - Add the PATH into ~/.bash_profile"
	@echo "make test - Test the genOpt"
	@echo "make clean - Delete all the pyc files in the ./lib"

clean: 
	-rm *.pyc
