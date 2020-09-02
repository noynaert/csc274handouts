# Linux Directory Structure

About a thousand people have already made videos about directory structures.  And they did it better than I would.  

[This is a good overview using a gui interface rather than command line](https://www.youtube.com/watch?v=HbgzrKJvDRw)  I suggest everyone watch this video ant try to duplicate what he is doing in a gui in the command line.  The notes below mostly follow this video.

[Here is an old but still good Nixie Pixel Video](https://www.youtube.com/watch?v=2qQTXp4rBEE) It covers several other things we have talked about.  I hope people who watch this keep thinking "Yeah, I already knew that."  Your tech skills are growing!

I like Chris Titus Tech. But it is pretty advanced in some ways  [Here is a link to a Chris Titus Tech video on directories](https://www.youtube.com/watch?v=roES8iAaJEM&t=725s)

## Windows 

* MS-DOS was only command line.
* Originally PC's only had two floppy disks called A: and B:.
* MS-DOS 2 brought in several innovations based around hard drives.  They needed directories because hard drives were so large.  They borrowed the Unix directory structure.  Also, A: and B: were already taken, so the hard drive became the infamous C: drive.
* Unix does not use drive letters.  The closest thing to C:\ in Unix or Linux is / (root)
* Windows is *not* case sensitive

## Directory structure

* Linux file structure is somewhat standard.  But different distributions will do some directories a little differently.  Also, Linux has changed over the years, especially the way they handle CDs, DVDs and USB drives

In Unix there are two meanings for "root."  One is the / directory which is the heart of the directory structure.

Root also refers to the superuser or main system administrator.  This user has a home folder called /root.  I think it was put there just to confuse newbies when someone talks about the "root directory."  When people talk about the root directory they usually mean /, not /root which is the root user's home directory.  (Ubuntu based systems do not allow a root user, but the functions of the root user are available to some other users.  The /root folder is also maintained.  Superusers tend to use the /root folder to stash important documents for the entire system.)

If you are watching the DorianDotSlash, I suggest you do ```ls /``` when the video starts.  He shows the root folder in a gui interface.  You will be seeing it in a command-line interface

* bin: Basic functions.  These are usually commands like ls that are needed if the system crashes.
* sbin: Basic functions only the superuser needs
* boot: Has your boot loader
* dev: Devices
* etc: System-wide configuration files and information
* home: User folders
* lib folders: These are compiled files that are used by programs
* media:  Where you look for USB sticks.
* opt: Manually installed software is installed here.
* proc: Files about resources used by the system.  Lots of fun to look in, but don't change anything
* root: The user's home folder
* run: A directory used for temporary storage
* sys: A temporary system set up by the system
* tmp: This is a temporary folder.  Users and the system often dump huge files here
* usr: This is where most programs installed with the system reside.  They are like /bin, except these files are not essential for system operation if the system crashes.  This can be a huge folder, so it is often on a different drive.
* var: Contains directories that are likely to grow large

## /home

Each user has their own directory in /home.  In other words /home/$USER

User's personal settings are stored in hidden files in the /home/$USER folder.


