# Unit 10.1 Script Inputs

## Reading from stdin

## Some more variables

* $# - How many arguments were passed to the Bash script.
* $@ - All the arguments supplied to the Bash script.
  * $0 - The name of the Bash script.
  * $1 - $9 - The first 9 arguments to the Bash script. (As mentioned above.)
* $? - The exit status of the most recently run process.
* $$ - The process ID of the current script.
* $SECONDS - The number of seconds since the script was started.
* $LINENO - Returns the current line number in the Bash script.