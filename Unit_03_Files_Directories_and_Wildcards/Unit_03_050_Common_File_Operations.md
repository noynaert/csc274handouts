# Unit 03_05 Common File Operations

## Finding and locating files

* ```find``` Helps you locate a file 
  * Takes 2 or 3 arguments
    * start directory.  
      * Use . to search from the current directory
      * use .. to search from the parent directory
      * use ~ to search from your home folder
      * -name followed by the file name.  May use globbing
      * -print Needed on some systems, but not generally Linux
* ```locate``` An easier way to find files, but it only updates at certain times (daily or more).  The superuser may update it manually with the ```updatedb``` command

## Some other commands

* Used with files and directories
  * chmod
  * chown
* Used with directories
  * du
  * df
  
[35 Linux Basic Commands Every User Should Know](https://www.hostinger.com/tutorials/linux-commands) Note that most deal with files and directories.

