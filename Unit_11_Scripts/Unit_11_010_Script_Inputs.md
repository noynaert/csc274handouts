# Unit 10.1 Script Inputs from Environment Variables

## Some more variables

* $\$ - The process ID of the current script.
* $@ - All the arguments supplied to the Bash script.
* $# - The number of parameters passed into the script
  * $0 - The name of the Bash script.
  * $1 - $9 - The first 9 arguments to the Bash script. (As mentioned above.)
  * ${10} for arguments more than 9
* $? - The exit status of the most recently run process.
* $\$ - The process ID of the current script.
* $SECONDS - The number of seconds since the script was started.
* $LINENO - Returns the current line number in the Bash script.

```bash
#!/usr/bin/bash
echo "The script name is \"$0\" and has a PID of $$"
echo "There are $# parameters"
echo "The full list of parameters was \"$@\""
echo "Argument 1 is $1"
echo "Argument 9 is $9"
echo "argument 10 is ${10}"
echo "This is line number $LINENO"
echo "This script is running for $SECONDS seconds"
sleep 3
echo "This script is now running for $SECONDS seconds"
```

## Script with a simple if/else

> if [[ *boolean* ]] 

>     then *statement* 

>     else *statement*

> fi

### freaky notation

There are three commands to do tests:

* ```test```
* ```[    ]```
* ```[[  ]]```

```test``` was the original way to test a boolean

```[``` is actually a command. Therefore the space after the [ is needed.  The [&nbsp;] notation makes some operations easier to write.  It works in most shells.

```[[ ]]``` is pretty much Bash only.  It would not run in sh or the Borne shell.  It handles a lot of messy syntax situations like null values and certain string problems.  It is built into the shell itself, and does not have a copy of the program in /usr/bin/


