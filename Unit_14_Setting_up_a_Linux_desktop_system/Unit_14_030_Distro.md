# 14.030 Distribution

This document is targeted at people installing Linux desktop for the first time.

I suggest that first-time (or even second-time) Linux users stay with Ubuntu or something that is derived from Ubuntu.  More experienced users may wish to branch out.

Reasons for staying in the Ubuntu family:

* Almost all major software is released for Ubuntu.
* If you have a problem or need to know how to do something there is almost guaranteed to be documentation about how to do it in Ubuntu.

* If you have a decent system
  * [https://ubuntu.com/#download](https://ubuntu.com/#download) and pick "Ubuntu Desktop"
* If you have an underpowered system
  * [https://kubuntu.org/](https://kubuntu.org/) for a somewhat underpowered system
  * [https://lubuntu.me/](https://lubuntu.me/) if it is really a piece of junk or a small hard drive
* Mint is a good choice as well, especially if you really, really liked Windows XP and Windows 7.
  * [https://linuxmint.com/download.php](https://linuxmint.com/download.php)
    * Pick the Cinnamon desktop in most cases
    * Go with XFCE if you are running on a piece of junk or have a small hard drive
* Elementary OSis a good choice for Mac users if you have a powerful enough system.
  * There is a lot of eye-candy.  It trades performance for pretty.
  * Get it at [https://elementary.io/](https://elementary.io/)  They have free and unpaid versions, but you have to hunt for the free
  * I do like it for laptops because of the "Picture-in-Picture feature.  You can simulate it in other desktops, but PnP on Elementary does it right and out-of-the-box.
* I have to mention [Pop! OS](https://pop.system76.com/).  I recommend it for CS majors who want something taylored for developers.  

## About [Linux Distributions](https://en.wikipedia.org/wiki/List_of_Linux_distributions#openSUSE-based)

* Debian
  * Ubuntu *et. al*
  * [Kali](https://en.wikipedia.org/wiki/Kali_Linux)  (Offensive Security, Penetration Testing)
* RPM, RedHat
  * Fedora
* Arch
  * Manjaro
* Others
  * Slackware
  * Gentoo
    * Chrome OS

## Debian Systems

Debian itself is a solid distribution

Debian systems install new software with a program called apt (or an older versions called apt-get and dpkg).  They are often called "deb" systems because the installation packages end with the extension ```.deb``` 

### Downstream from Ubuntu

Ubuntu is derived from Debian.  However, Ubuntu keeps its own repositories for software.  Therefore things may be available for pure Debian systems.

## Current state of affairs in my book

For students and first-time Linux users, I think it is best to stay "downstream" of Ubuntu.

There is a lot of documentation on Ubuntu systems.  That can be important to students.  Most of the time the explanation for Ubuntu will apply to systems that are downstream from Ubuntu.

I feel like Ubuntu is turning into the evil Microsoft of the 1990s. Ubuntu has done a lot of controversial things.  One of the bad ones currently is the Snap system.  Ubuntu is very committed to Snap for installing software.  In my experience it is slow.  It is also completely controlled by Ubuntu.

Most systems derived from Ubuntu have fixed Snap (by removing it) and re-enabling competing technologies such as Flatpack and AppImage.

Here are my recommendations:

If you have a machine you do not want to duel boot and it is a very modern, well equipped system (i5 or better, 16 or more Gig of RAM, decent video card) then use PoP_OS.  That is what I have used all semester.  It is on my main desktop computer.

If you are a new user or if you are going to dual boot, or if you are going to install on a weaker computer then I recommend Cinnamon Mint.  It is known as a beginner's system, but lately it has gotten a lot of respect as a strong voice that is not Ubuntu.  I had to buy a new laptop recently.  It is a powerful system.  I know what I am doing in Linux.  But I went with Linux Mint instead of Pop because I wanted to make it easier to dual boot.

There is a new and interesting kid on the block (well, not that new.  It is in version 5.  But it is getting a lot of notice.)  Linux Mint has a release of "Linux Mint Debian Edition."  They have made a version of Mint that is based on Debian, not Linux.  It seems to be catching on.   I am currently in the process of setting up a server at home.  I bought a decent used computer on Ebay for $50 plus $21 in shipping.  I do not plan to dual boot (it didn't come with Windows)  I am going to put LMDE on it.  I would have put it on my laptop, but there are still a lot of dual-boot issues with it.  But for this little server it is perfect.  



