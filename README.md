# PHP-to-Python

PHP variables into Python scripts

In this repository we will understand how to pass variables in PHP and Python

First create two different file, sender.php and receiver.py

Next, in those two file there is some functions that we needed also to understand :

In PHP, 

exec() ~ Executes the given command.
shell_exec() ~  Inbuilt function in PHP which is used to execute the commands via shell and return the complete output as a string.
escapeshellcmd() ~ Escapes any characters in a string that might be used to trick a shell command into executing arbitrary commands.
escapeshellarg() ~ Escapes any existing single quotes allowing you to pass a string directly to a shell function. 

In Python,

import sys ~ Python provides various functions and variables that are used to manipulate different parts of the PRE.
sys.argv[list count] ~ Python list that contains the command-line arguments passed to the script.

