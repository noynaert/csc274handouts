# Unit 08.015 Another way to get hardware information

## lsxx commands

Another way to get information about the system is with the "lsxx family" of commands.  These often pull from /proc directory folders.  Some of the commands are restricted to super users or sudoers, and some provide only limited information to regular users

The various command have developed over time and have different uses.  Some are more developed because they are used extensively.  Therefore do not assume that the options for one command are used by other commands.  Always check the man page if in doubt.

## `lshw`

The `lshw` provides a summary of the system.  It is very handy for doing inventory, especially because it can output in a number of database-friendly formats such as .json, .xml, and even as a mysqllite database.  

## Other lsxx commands

* `lscpu`  Information about the CPU
* `lsusb`  Information about the usb busses and the attached devices.  This is commonly used to diagnose problems with peripherals because it pulls together a lot of information that are scattered across a lot of different /proc entries
* `lsblk` Information about all the attached block devices
* `lsdev` This provides data about /dev devices.  This includes a lot of things like interrupts that are not listed in /proc.  On some systems `lsdev` must be installed  
