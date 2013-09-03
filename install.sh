#! /bin/bash

cd ..
filepath=$(pwd)/.local/bin
if [ -d $filepath ]; then
	cd genOpt
	cp genOpt.py $filepath/
	cp configTypes $filepath/
else
	mkdir -p $filepath
	cp genOpt.py $filepath/
	cp configType $filepath/
fi

cd ..
libpath=$(pwd)/.local/lib/python
if [ -d $libpath ]; then
	cd genOpt/lib 
	cp *.py $libpath/
else
	mkdir -p $libpath/
	cd genOpt/lib 
	cp *.py $libepath/
fi
