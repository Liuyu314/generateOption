# generateOption

This program is used to generate the option in files.

## Installation & Running

    git clone https://github.com/Liuyu314/generateOption.git
    cd generateOption
    make

Maybe you have to exit the terminal and open it again.   
If there are some problems about the permission, check the permission of system or the permission of files.    

## Testing
If you want to run the testing, input:

    make test

Then check the ./tests.

## Usage

    genOpt file1.c
    genOpt file2.py
    genOpt file3.scm
    genOpt file1.c file2.py file3.scm

## Response
This project is under development, it can only generate the option for Python, Scheme and C language. If you are interested in the project, join it and develop some features for other languages.

Here are some response:

C:

    /****************************************************
     *    Author:  UserName
     *    Email:  UserEmail
     *    Time: 2013,09,04 22:22:01
     *    Description:
     *    Version:
     *    Option:
    ****************************************************/

Python:

    # Author:  UserName
    # Email:  UserEmail
    # Time: 2013,09,04 22:03:44
    # Description:
    # Version:
    # Option:

Scheme:

    ; Author:  UserName
    ; Email:  UserEmail
    ; Time: 2013,09,04 22:03:44
    ; Description:
    ; Version:
    ; Option:

## Other Details

    make help

## License

MIT License
