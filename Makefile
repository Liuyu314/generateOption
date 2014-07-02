.PHONY: install clean clean-test test

install:
	echo "export PATH=$(shell pwd):$$PATH">>~/.bashrc
	echo "export PYTHONPATH=$(shell pwd)/lib:$$PYTHONPATH">>~/.bashrc
	./install.sh

uninstall:
	@./uninstall.sh
	@echo "uninstall success!"

test:
	@./test.sh
	@echo "===================Testing===================="
	@echo "Compare to the cmptestfile..."
	@echo "If the testing is ok, there's no output..."
	@diff cmptestfile testfile
	@echo "=================Testing End=================="

help:
	@echo "make (install) - Add the PATH into ~/.bash_profile"
	@echo "make test - Test the genOpt"
	@echo "make clean - Delete all the pyc files in the ./lib"

clean: 
	-rm lib/*.pyc
