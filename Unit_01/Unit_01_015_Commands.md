# Commands
## Commands in this lesson

Some of these commands will be covered in the videos, and some in the assignments.

I suggest you note what each of the following does as you go through the videos.  Before taking the quiz use the "man" utility to figure out what the other commands do.  (Using man will be covered in one of this unit's videos.)

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
* passwd
* mkpasswd
* cal
* ping
  
## Keystrokes used in this lesson
  
* Ctrl-c
* Up-arrow
* tab
  
## Commands

* case sensitive
* often terse or parsimonious
  * old commands are often 2 or 3 letters
  * often no unneeded output.  Sometimes none
  
  ![Teletype machine](images/teletype.jpg)

## Strings

  There are several ways to make strings  For right now we will only talk about three ways

* Naked
  * Best used when there are no spaces or punctuation
  
```bash
$ echo Hello
$ cowsay Hello
```

* Single Quote '
  * an apostrophy to a normal human
  * may be used around single words
  * more efficient than double quotes
  * useful when the string includes double quotes
  * **Best practice is to get in the habit of using single quotes**

```bash
$ echo 'Hello, World'
$ cowsay 'Hello, World'
$ cowsay 'Hello, $USER'
$ cowsay 'He said "Where is Dave?"'
```

* Double Quote "
  * just a normal quote mark to a normal human
  * may be used around single words
  * less efficient than double quotes
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

Now try the following while logged into turing

```bash
$ ping www.missouriwestern.edu
$ ping turing.cs.missouriwestern.edu
```

## Pipes Interlude

Pipes will not be on this quiz.  Pipes will be covered in a later unit.  
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
```

Reminder.  Pipes will not be on the Unit 1 quiz.  But they are useful and pretty easy.
