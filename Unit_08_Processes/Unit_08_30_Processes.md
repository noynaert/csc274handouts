# Unit 08.30 Processes

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

For a non-root user, ```ps -x``` is useful for seeing all your processes from all terminals



