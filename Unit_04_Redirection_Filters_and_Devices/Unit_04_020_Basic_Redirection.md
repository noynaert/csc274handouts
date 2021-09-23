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


### Redirect stdout

The > symbol sends stdout to a file instead of the console.

* ```date > now.txt``` sends the stdout from the date command into a file called now.txt.

* Redirection works *right* to *left*
* If the file exists, it is erased
* /dev/stdout is the first device sent to the terminal, so we could do the following
* ```date 1> now.txt```

#### Using ```cat``` to create files

The ```cat``` command reads a file and prints it to the screen.  But cat can be used to create a file when you are too lazy to start an editor.  Just be sure to remember that ^d at the start of a line is the flag for EndOfFile (or EOF)



### Redirect stderr 

The 2> symbol(s) directs stderr to a file.

For example, the command ```find / -name moby.txt``` generates so many errors it is hard to find the data you are looking for.  However, the command ``find / -name moby.txt 2> errors.txt``` sends the stderr stream into the file "errors.txt."

There are variations here.  For example, ``find / -name moby.txt 2> errors.txt > results.txt``` sends stderr to errors.txt and sends stdout to results.txt.

#### Another way to send data to stdout that is rarely used

```bash
cowsay -f tux "I am Tux." 1> tux.txt
```

### Redirect both stdout and stderr to the same file

The old way to do this was like the following:

```bash
find / -name moby.txt > results.txt 2>&1
```

The above method looks backwards and unintuitive to a lot of people (including me).  I would like to write it as something like ```ls> results.txt  2>&1 ```

The problem is that > works from right to left., which also looks backward unless you remember that it works right to left.

Also, the ```2>&1``` syntax is not easy to remember. But it is only in Bash as of now.

The new way is to use the following.  I recommend it, although there are a few wierd cases where it does not work.  

```bash
ls &> results.txt
```

### Pipes

The Pipe command redirects the output of one command into the input of another command.

The symbol for pipe is `|`.  It is usually right above the "Enter" key on the keyboard.  It is usually the shift-\ key.  The symbol is called the "Vertical Bar."  On many keyboards the actual symbol shown is `¦` which is technically known as the "broken bar"

Example:  
   * The date command sends output to stdout.
   * Cowsay takes input from stdin and sends the results to stdout
   * The command ```date | cowsay``` has the date command redirect its stdout to the stdin of cowsay

## Appending output

If you use a single ```>``` any existing data in the file is erased.  If you want to *append* output to an existing file, use ```>>```

## Redirecting Input

As you might guess, ```<``` is used to  send a file to a command.  As you might not guess, the input file is the last thing on the line.

```bash
cowsay < stuff.txt
```

The input comes after the output, which is opposite of the normal unix "fromt to" format.

```bash
cowsay > moo.txt < stuff.txt
```

## Things that are not redirection, but kind of feel like it

### Line continuation

The ```\``` key by itself means the command continues on the next line

### Chaining

Some of the chaining commands feel like piping.  But they are not.  The output from one is not redirected to the next command in the chain

*  ; 
  * allows 2 commands on the same line
* ```&&```  
  * Be careful not to use a single &, at least in this chapter
  * && means only execute the second command if the first succeeds
* ```||```  
  * || is a "logical OR"  
  * This is kind of the opposite of &&
  * || means only execute the second command if the first command *fails*  It gives you a fallback option.
  ```
        ls *.xyz || echo 'No .xyz files were found'

Yes, you can combine chaining and pipes.


More for those who want to go deeper: [10 useful chaining operators](https://www.tecmint.com/chaining-operators-in-linux-with-practical-examples/)
