# Unit_04_020_Basic Redirection

## Three devices of special interest

* /dev/stdin  -- The place a program gets input from
* /dev/stdout -- The place a program sends normal output to
* /dev/stderr -- The place a program sends error messages

When we talk about them we talk about stdin, stdout, and stderr.  We talk about them so much we just drop the /dev

Exactly what these devices are depends on the context.  The context we are most concerned with is being logged in at the console.  Therefore they are assigned as follows by default:

* stdin is the keyboard
* stdout is the display, or "console"
* stderr is also the display or console.

Most programs are set up in two different ways.  By default they read from stdin and print to stdout.  Many programs will also take input from the command line or from a file.  But the way they usually do this is by sending the command line argument or the data from the file to stdin.

## Redirection

redirection causes something other than the keyboard to be used for input.

### pipe

We have seen the Pipe command.  

Example:  
   * The date command sends output to stdout.
   * Cowsay takes input from stdin and sends the results to stdout
   * The command ```date | cowsay``` has the date command redirect its stdout to the stdin of cowsay

### Redirect output

The > symbol sends stdout to a file instead of the console.

* ```date > now.txt``` sends the stdout from the date command into a file called now.txt.

The 2> symbol(s) directs stderr to a file.

For example, the command ```find / -name moby.txt``` generates so many errors it is hard to find the data you are looking for.  However, the command ``find / -name moby.txt 2> errors.txt``` sends the stderr stream into the file "errors.txt."

There are variations here.  For example, ``find / -name moby.txt 2> errors.txt > results.txt``` sends stderr to errors.txt and sends stdout to results.txt.


