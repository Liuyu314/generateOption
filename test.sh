#! /bin/bash
# This code is just for testing.
# Run this code by "./test.sh"
# Or "make test"

if [ -f "./tests/hello.c" ]; then
	echo > "./tests/hello.c"
fi
if [ -f "./tests/hello.py" ]; then
	echo > "./tests/hello.py"
fi
if [ -f "./tests/hello.scm" ]; then
	echo > "./tests/hello.scm"
fi
if [ -f "./tests/hello.sh" ]; then
	echo > "./tests/hello.sh"
fi


if [ -f "./testfile" ]; then
	echo > "./testfile"
fi
genOpt ./tests/hello.c >> testfile
genOpt ./tests/hello.py >> testfile
genOpt ./tests/hello.scm >> testfile
genOpt ./tests/hello.sh >> testfile
genOpt ./tests/world >> testfile
genOpt ./tests/hello.com >> testfile
genOpt ./tests/hello.c ./tests/hello.py ./tests/hello.scm ./tests/hello.sh >> testfile
genOpt ./tests/hello.c ./tests/world ./tests/hello.com ./tests/hello.sh >> testfile
