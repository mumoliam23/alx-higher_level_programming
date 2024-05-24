0x00. Python - Hello, World

0. Run Python file
A shell script that runs a python script.
'#!/bin/bash' instructs the system for execution using Bash shell.
python3 is the command used to run the python interpreter
"$PYFILE" reference value of environment variable.
Set the argument PYFILE to main.py and run the script (export PYFILE=script.py)

1. Run inline
A shell script that runs a python code
'#!/bin/bash'
'python3 -c "$PYCODE"'
-c allows the python interpreter intepret a string as a script file name an execute it
