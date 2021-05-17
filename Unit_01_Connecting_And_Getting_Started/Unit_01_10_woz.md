# Unit 01.10 Woz


## Choices

A Unix or Linux course can be taught several ways

* Students use computers in an on-campus lab
* Log into a remote system
* Students use Raspberry Pi systems
* Students use virtual machines
* Students dual boot their laptops or use recycled laptops
* Use a cloud system

## Our working environment for the first part of the course

### Motivations

In the first part of the semester we will be connecting to the same server.  
There are several reasons for this:

* Easier setup for students at the start of class
* Everyone is working in the same environment
* Students may use the server for other classes
* The environment is less likely to be damaged by a sudo accident.
* Remote server is a realistic working scenario
* We can have some fun.

### woz.cs.missouriwestern.edu ![woz.cs](images/turing.jpg)

### Terms that mean about the same thing:  

* terminal window 
* console 
* command prompt 
* CLI (Command Line Interface)

## Connecting

### SSH

SSH is a *protocol* for how to connect to a computer.  It is a set of guidelines about how a local computer can open a console on another computer.  

There are several programs that implement the ssh protocol.  In the background they use the protocol.  They allow the human at the keyboard connect to use the connection between computers.  Examples include the following:

* Bitvise
* Putty
* ssh (this is a command that may be used on Windows 10 system, Linux, and Mac.  The program also uses the SSH protocol in the background.

### Actually connecting

The way you connect will depend largely on your operating system.

* Mac and Linux:  You should be able to use the ssh command.  See the page on ssh.
* Windows:  I recommend that Windows users start using either "Putty" or "Bitvise."  If you have a late version of Windows 10 with WSL2 installed you may also be able to use ssh directly from a command prompt.  But if you are already kind of lost I suggest you start with Putty.
* Bitvise:  This is probably a better option for Windows users than Putty.  Putty is an older program, but it does have some useful utilities with it.  I suggest loading both.

#### Downloads for Putty and Bitvise

* [Putty at https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
* [Bitvise at https://www.bitvise.com/download-area](https://www.bitvise.com/download-area)  You should only get the client.  *Do not download the server.*

### Login Id and password

Your login should be the same as your Missouri Western goldlink login id.

Your password will be provided by your instructor

In the following examples, the userid is *abyron* but yours will be different
