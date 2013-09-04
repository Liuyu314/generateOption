.PHONY: install clean clean-test test

install:
	echo "export PATH=~/generateOption:$$PATH">>~/.bash_profile
	echo "export PYTHONPATH=~/generateOption/lib:$$PYTHONPATH">>~/.bash_profile
	source ~/.bash_profile

test:
	./test.sh

help:
	@echo " "

clean: 
	-rm *.pyc
