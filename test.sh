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

genOpt ./tests/hello.c ./tests/hello.py ./tests/hello.scm
