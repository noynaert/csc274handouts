# Unit 08.40 Foreground and Background (with killing)

Each terminal may have one program in the foreground.  It may have many programs in the background.

## Putting programs in the background

* Putting & after a command throws the process into the background immediately.
* ^Z puts a running job into the background

Try ```sl &``` and then ```ps -x```.  Then give the ```fg``` command.  Can you do ^z and fg multiple times?

* BEING IN THE BACKGROUND DOES NOT AUTOMATICALLY MEAN STOPPED

Why would we want to put programs in the background?

* Debugging
* Gui programs sometimes have useful output while they are running
* Gui programs that don't have useful output may freeze the terminal
* Sometimes a process will be slow, but doesn't need much attention, such as a complicated ```sed``` script

## Killing

Sometimes we need to kill a running process.

"Killing"  doesn't really mean "killing."  It is more like sending a process an order to commit suicide.  In most cases the program has a chance to clean up after itself.

### Signals

* ^C sends the INT signal (INTerupt)
* ^Z sends the TSTP signal (TerminalSToP)

Number | Name | Meaning
---|---|---
1 |HUP| Hang Up.  It used to literally mean "Hang up the phone" for dial-up modems.  It sends a signal that the terminal is stopped.  In SSH, it is equivalent of shutting down Putty, Bitvise, or the ssh command.
2 | INT | Signal that the program should quit.  
9 | KILL | The program cannot ignore a kill.  It does not get to clean up after itself
10 |TERM| The default signal from kill.  The program only gets this if it is in the running state
20 | TSTP| Basically, ^Z
18 | CONT| restores a process after a stop
19 | STOP | This causes a program to pause without terminating.  It cannot be ignored

## ```kill``` command

```
kill 29424
kill -1 29424
kill -INT 29424
```

## ```killall```

Kills many programs by name.  Also may kill by user.