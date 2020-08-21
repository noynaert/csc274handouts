# Commands
## Commands in this lesson

Some of these commands will be covered in the videos, and some in the assignments.

I suggest you note what each of the following does as you go through the videos.  Use the "man" utility to figure out what the other commands do.  (Using man will be covered in one of this unit's videos.)

* whoami
* exit
* echo
* cowsay
* figlet
* date
* cal
* finger
* ls
* wget
* chfn
* finger
  
## Keystrokes used in this lesson
  
* Ctrl-c
* Up-arrow
* tab
  
## Commands

* case sensitive
* often terse or parsimonious
  * old commands are often 2 or 3 letters
  * often no unneeded output.  Sometimes none
  
## Strings

  There are several ways to make strings  For right now we will only talk about three ways

* Naked
  * Best used when there are no spaces or punctuation
  
```bash
$ echo Hello
$ cowsay Hello
```

* Single Quote '
  * an apostrophe to a normal human
  * may be used around single words
  * stronger than double quotes
  * useful when the string includes double quotes
  * **Best practice is to get in the habit of using single quotes**

```bash
$ echo 'Hello, World'
$ cowsay 'Hello, World'
$ cowsay 'Hello, $USER'
$ cowsay 'He said "Where is dave?"'
```

* Double Quote "
  * just a normal quote mark to a normal human
  * may be used around single words
  * more lenient than double quotes, especially if $ symbols are involved.
  * useful when string includes apostrophe "Dave's not here."
  
```text
   Hit the up arrow once and change the single quotes to double
$ cowsay "Hello, $USER"
$ cowsay 'Hello, $USER'
$ cowsay  Hello, $USER
```

### Getting out of trouble with Ctrl-c

It is easy to forget a closing quote mark.  If that happens it may look like the
 system is hung up.  Don't panic.  Hold down the Ctrl key and hit c.  Ctrl-C is
 often called ***"Break"*** and can be your best friend.

Type the following command.  It measure verifies that we have a network connection
 and measures the time it takes to send messages to computer.  
(There are a thousand milliseconds in a second, so 100 ms would be a tenth of a second.)

$ ping example.com

The problem is the command runs forever.  Hit Ctrl-c to break.

Now try the following while logged into woz

```bash
$ ping www.missouriwestern.edu
$ ping turing.cs.missouriwestern.edu
```

## Introduction to man pages

```bash
$ man cowsay
```

* For now, read the description
* Look at the options that start with -
* Use the PgDn and PgUp keys to move through the file.
* Try the -d option.  Then try some of the other options.

Do some experimenting.  Have some fun.  Try using more than one of the options at the same time.  Are there any that don't make sense to use together?

Look at the listing produced by *cowsay -l*

Now try using the -f command with the list of files from -l

The website https://github.com/paulkaefer/cowsay-files/tree/master/cows is proof that some people have too much time on their hands.  Try the two following commands

```bash
wget https://raw.githubusercontent.com/paulkaefer/cowsay-files/master/cows/dilbert.cow
cowsay -f ./dilbert.cow 'TGIF'
```

### Another command to investigate

```bash
$ man date
```

Some options start with --.  This is a new style that was in vogue for a while.  Now it is mostly used for documentation when you look at tutorials.

## Pipes Interlude

Pipes will not be in this unit.  Pipes will be covered in a later unit.  
However, in this unit we will introduce using them.  Hopefully they will
not feel as odd when we get to them.

Most commands can take their input from the keyboard and send send output to the screen.

Commands can be combined with a | (or "pipe") symbol.  It is usually on the
right side of the keyboard above the enter key.

Try this:

``` bash
$ date
```

Now "pipe" the output of the date command as input to the cowsay command.

```bash
$ date  |  cowsay
$ fortune
$ fortune | cowsay
$ figlet 'Hello'
$ figlet 'Hello' | cowsay
$ figlet 'Hello' | cowsay -n
$ date | figlet | cowsay -n
```

## Other characters on the keyboard

* Ctrl-C for break.  Ends most programs.  Sometimes hitting the Esc key or Ctrl-D also works
* Up arrow goes back in the command history.  This is handy when you need to repeat or edit a command
* Tab is used for "Tab Completion."  It attempts to fill in a command or file name.  The way most email programs try to fill in email addresses was inspired by this.
