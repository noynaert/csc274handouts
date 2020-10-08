# Unit 08.30 Processes (warning, Zombies ahead 🧟)
##

Reference: [https://www.theunixschool](https://www.theunixschool.com/2012/09/what-is-process-in-unix-linux.html#:~:text=A%20process%20is%20a%20program,binary%20executable%20or%20any%20application.)

When a program "loads" it is moved from Secondary Storage to Primary Storage (that is, from Disk to RAM)

## Process

* A ***process*** is a program in execution
    * It has been loaded into RAM
    * Most, but not all commands create processes.  Some commands like "ls" are built into the terminal
    * Two forms of processes:
        * Spawned from a terminal
        * Daemons -- Running independently of any terminal session
            * Generally services running in the background such as httpd, sshd, fingerd
        
Process attributes

* **PID** Process-id -- Given a number starting at 1.  The longer a computer is up, the bigger the PID.  PIDs can be reused
* **PPID*** Parent Process ID  -- Every process except the first ```init``` command has a parent
* ***TTY***  Terminal process associated with a process. -- TTY refers to "teletype"
* ***UID*** User Id -- The user who can kill the process (or the root user, or a sudo user)

## ```ps``` 

PS has different flags in BSD and other standard unixes.  Linux includes both.  Standard unix versions have a dash, BSD commands do not.  Gnu (two-dash) format is also supported.

```text
  [abyron@woz ~]$ ps
    PID TTY          TIME CMD
  29193 pts/6    00:00:00 bash
  30307 pts/6    00:00:00 ps
```

* PID -- The process id.  Note how much it has gone up just since you logged in!
* TTY -- Short for "teletype."  I think the pts means it is using ssh port #6.
* TIME -- the amount of CPU time being used.  Not very much, in the above examples.
* CMD -- Command used

### ```ps -x```

For a non-root user, ```ps -x``` is useful for seeing all your processes from all terminals

Note that some processes are not attached to terminals (TTY)

STAT is short for "State"

* R  Running, or could run if it had the CPU
* S  Interuptable Sleep (probably waiting for a keystroke)
* Ss Uninteruptable Sleep (probably has a child state)
* D Waiting for the hard drive (Another form of Ss)
* S Stopped
* Z Zombie state (process has terminated, but parent has not yet cleaned it up)
* N Nice  It is set to be low priority
* < Not Nice  -- set to run at higher than usual priority



