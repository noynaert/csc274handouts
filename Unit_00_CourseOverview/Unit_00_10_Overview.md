# Unit 00.10 Overview

# Unix and Linux

## Unix is an operating system like Windows.  

* Operating System is the "software that controls the software"
* OS takes over during bootup
* OS launches other programs and cleans up afterward
* OS provides services like access to printers and files on the disk
* OS provides security services

## Very, very brief history that still effects us now

How Unix was developed | A teletype
-----------------------|-----------
![Thompson and Ritchie at PDP-11](/Unit_00_CourseOverview/images/1920px-Ken_Thompson_sitting_and_Dennis_Ritchie_at_PDP-11.jpg) | ![A teletype machine showing the peg-style keyboard and paper](/Unit_00_CourseOverview/images/teletype.jpg)

CRT terminals were not available at that time.  Teletypes were the most common interface.  The use of teletypes had a couple of implications for us today:

* The only interface was text-based.
* [Parsimonious](https://www.merriam-webster.com/dictionary/parsimonious) input.  
  * It was relatively slow to type on, so short commands are favored.
  Not much memory or storage.  Every byte counted.  (They used pure ASCII, so 1 character meant equaled 1 byte)
* Parsimonious output.  
  * Don't waste paper and cause scrolling by printing anything that is not immediately useful.
  * Make provisions to get additional information on-demand (with parsimonious typing, of course)
* Very few special characters on the keyboard.  Also, no arrows or movement commands.
* 80 column width
  * 80 columns was inherited from an older technology known as [punched cards](https://upload.wikimedia.org/wikipedia/commons/f/f3/Punched_card.jpg) had 80 columns.  We typed them on [card punch machines](https://www.youtube.com/watch?v=YnnGbcM-H8c)  (I spent many hours at an IBM Model 29 keypunch when I was a student.  Being able to use a keypunch machine got me my first computer job).

  ### Dumb Terminals

  ![A CRT Dumb Terminal](/Unit_00_CourseOverview/images/hpDumbTerminal.jpg)
  
  Dumb Terminals replaced the teletype.  This was the model used on our campus until about 1990.

* No CPU.  They were just a keyboard and monitor that connected to a remote computer somewhere.
* Still not fun to type on, but better typing than teletype
* No cost of paper, but only 24 or 25 lines.  So parsimonious output is still important.
* No color.  Either green on black or orange on black.
* No Graphics other than ASCII Graphics.
  
  ![ASCII Graphics](images/asciiArtSmall.png)

# Unix Shell

The shell is what we type into.  It is a program that takes input from the keyboard, passes it to the *kernel* and displays the output to the screen.  The shell is the interface between the user and the operaating system.

Historically there have been different shells that were used.

* ***sh*** was the original shell
* ***Bourne*** added a lot of advance features.  It was licensed and a closed source program.
* ***Bash*** The "Bourne Again SHell" is an open-source version of the Bourne shell.  It adds some features and has been optimized to run in terminal emulators.  It has provisions for color.  Bash runs on most modern Unix systems, including linux.

# Linux

* Linux is a version of Unix
* Releasted under the GNU open-source license
* Linux is actually just the ***kernel*** or core program that is the Operating System
* Android phones and Chromebooks use the Linux kernel
  * Therefore they are technically Linux
  * They have an entirely different shell (Interface) but they are still Linux.
    * There is an experimental way to load Bash on a Chromebook.
    * You can load bash on your Android, even without Rooting your phone
    * ![Bash on Android](images/BashOnAndroidSmall.png)

# This Semester

* Most of this semester we will focus on Bash.
* The focus will be Linux-centric.  However, you can also apply it to other Unix-type systems such as Mac.  Much of the material will apply to Bash running on those systems.
* You will *not* need to run Linux on your own computer until late in the semester.
  * You are welcome to do so, however.
    * Use an old computer.
    * Dual Boot (higher risk).
    * Rapberry Pi or something similar.
