# Unit 02.050 Installing new commands

## Distributions

Different distributions of Linux use different commands to install new software.

For now you don't need to know all of these distributions. But you do need to know that there are different distributions. You should know that the woz.csmp system is running Ubuntu which is running Fedora which is an rpm-based system. The different distributions all worm much the same, but they will have different ways of installing software.

Three main types of distributions

- Debian Based (.deb)
  - Debian
  - Ubuntu, Kubuntu, Lubuntu, etc
  - Mint
  - Pop!
- Red Hat (.rpm based)
  - Red Hat
  - Fedora
  - Suse
- Others
  - Arch
  - Slackware

### Apt

- apt or apt-get for .deb distributions
- dnf or yum for .rpm distributions

### New kids on the block:

- snap
- flatpack
- appimage

## "Admin" or "Superuser"

Installing some commands requires you to be an administrator on the system. An administrator is called the "superuser." The administrators are referred to as "super users." On the woz.csmp system most students are not super users, but if you install Ubuntu on a laptop you will have super user rights.

## Root user

There can be many users who can be super users. There is one special superuser named "root."

On most Linux systems it was possible for the root user to log onto the system. However, Ubuntu changed the game a bit by not allowing "root" to login. Root still has a folder. But no one can log in as root.

Distributions that are "downstream" from Ubuntu do not allow root logins. This includes Mint and Pop!.

Preventing Root from logging on is a large security improvement.

- The "root" user is an obvious target for hackers
- If a user is logged in as root it is too easy for them to damage the system while they are operating as a regular user.

Although most non-ubuntu distributions allow login as root, many network servers do not allow root to log in remotely via ssh or an older system called telnet. A lot of servers operate in "headless" mode, so effectively this prevents root login

## `sudo`

Superusers who are not root may use the `sudo` command to do actions that require root access. "Sudoers" are users who are authorized to use sudo.

The `sudo` command is placed before another command. So, for example, the command to update the system is `apt update`. The root user could just do this command. However, a regular user would need to type `sudo apt update`. Go ahead and try `sudo apt update` on woz. Relevant XKCD Cartoon](https://xkcd.com/838/)

[Another relevant XKCE Cartoon](https://xkcd.com/149/)

### Sudoer authority

It is possible for sudoers to be able to do everything a root user can do. Or sudo authority may be limited to just certain tasks. This increases security. If you have several people who do various administrative tasks, each person can have just their level of authority assigned to them.
