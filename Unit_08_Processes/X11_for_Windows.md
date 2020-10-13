# X11 Server for Windows

## X11

* The X11 package allows running GUI applications from a local *or remote* server
* Not a full desktop, especially when run remotely
* The X11 terminology is backward from every other application
  * The "server" runs on your local machine
  * The "client" runs on the remote system
  * This kind-of-sort-of-makes sense when you look at the mechanics of what is going on

## X11 security

X11 is itself very insecure.  It was developed in an era when you could assume that only nice people were on your network.

Now we combine SSH and X11 to make X11 more secure. 

* We "tunnel" X11 through an SSH connection.  
* SSH calls this "X11 Forwarding"

## Who Needs X11

### Mac and Linux
    Mac and Linux users almost certainly have it installed already

    If you start X11 through the command line, your new command line will need to have the -X parameter.  X is capitalized.

```
        ssh -X abyron@woz.cs.missouriwestern.edu
```

In October 2020 Windows started making an X11 server available in Windows 10.  I hope this means I will be able to delete these notes soon.  (Written in October 2020, and the X11 server is still propagating.  It probably will not show up in the labs until next semester at the earliest.)

## Solutions for Windows users

There are several solutions available

* **xming** 
    * This is an old program, but it works.  It hasn't been updated since 2016, so I worry about security issues
    * [https://sourceforge.net/projects/xming/](https://sourceforge.net/projects/xming/)
* **Cygwin**
    * Cygwin is a massive system that we used to use to run a unix-like environment on Windows.  
    * The Windows Subsystem for Linux is making cygwin irrelevant.  The X11 server is probably the biggest reason people still load it
    * Cygwin is slow to install, and still isn't really transparent.
    * This is what Bitvise recommends.  They provide instructions at https://www.bitvise.com/ssh-x11-forwarding

## Using the server

You must start your server (either xming or Cygwin) before you log onto woz with Putty or Bitvise.

### ssh from a console

```bash
        ssh -X abyron@woz.cs.missouriwestern.edu
```

### Bitvise

Go to the "Terminal" tab.  Check the box to enable X11 Forwarding

### Putty

You must authorize X11 forwarding.  Be sure to save the session after you make the changes.

* Find "SSH" under "Connection"  Click on the + next to SSH
* Just check the box for X11 Forwarding.
* Close that window and get back to the main Putty Window.
* Click on "Session" and then save the Session

First Screen|Second Screen
---|---
![images/x11.png](Pick Sessions and X11) | ![images\x112.png](Enable x11 forwarding)

