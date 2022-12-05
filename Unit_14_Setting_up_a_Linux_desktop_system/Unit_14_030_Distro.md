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

My default answer for everyone is Linux Mint unless there is a reason not to.  

Linux Mint has a reputation as a good implementation for beginners.  And that is well deserved.  It installs with a minimum of fuss and doesn't sweat philosophical issues about things like proprietary drivers.  The objective is to get a system that install and runs on just about any piece of computer junk you have lying around.

But lately Linux Mint has gotten a lot of favorable attention.  They are downstream of Ubuntu, but in many ways they are taking effective stands against Ubuntu.

The default desktop for Linux Mint is their own "Cinnamon" desktop.  I don't particularly like it.  I suggest you try it out.  It is basically like Windows 7.  If you don't like it you can install another desktop.  I like Windows Managers and KDE Plasma.  Those can be added to Linux Mint later if you want.  You can also add the standard Gnome desktop.

Linux Mint is a good choice as long as *any* of the following conditions are met.

* You want to dual boot
* You are a novice at Linux
* Your hardware is older.  Mint will run very well on systems laptops that run Windows 7.  It will even run well on some systems that are older than that.
* You are not running a public server

There are other Linux distributions that are good if you have special conditions

My main desktop computer runs PoP_OS.  It is great for developers.  The two major downsides are that it requires fairly high-performance hardware and it does not automatically set up dual booting.  My computer was bought for me to do schoolwork on, and it is fairly high-end.  I did want to preserve the Windows system that came with it, and I was able to fiddle with the boot system to enable dual booting.  

If dual booting isn't required, then I suggest LMDE.  I just bought an EBay used desktop computer for $50 plus $21 shipping.  It has 16 Gig of RAM, and older I7 processor, and 500GB hard drive.  I am going to use it for a home server for running NextCloud and our holiday displays as well as miscellaneous household automation tasks.  Dual booting isn't a problem.  LMDE is an project being done by Linux Mint.  The LMDE ditches Ubuntu entirely and goes builds off Debian directly.  The current version does not dual boot very well.  But my $50 computer came without Windows, and generally I have no need for dual boot on that system.

If you are setting up a public server, then I suggest something in the Red Hat family.  That will generally provide the best security.  Pure Red Hat is a great choice for a server if you can afford it.  Fedora is another choice.  It has good security, but it isn't as stable as Red Hat.  (Woz runs Fedora).  If you don't want to pay for Red Hat and want a stable server, then CentOS or SUSE are good choices.
