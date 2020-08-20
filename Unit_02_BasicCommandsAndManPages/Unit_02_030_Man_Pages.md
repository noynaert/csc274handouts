# Man Pages

In preparation for this exercise do the following command:

```bash
wget http://webservices.missouriwestern.edu/users/noynaert/moby.txt
```

This fetches a large text file we can use to play with.

## More or Less

More is an old (and outdated) program for stepping through large text files one page at a time.

```bash
$ more moby.txt
```

* Use q to quit

Less is the replacement for more.  Still uses the same commands, but lets you go backward in the file.

```bash
$ man less
$ less moby.txt
```

In this type of man page we are not really looking at the options.  We are looking at how to use the commands.

The first warning on the less page is that the commands are based on "vi"

### ***I suggest that you open two ssh windows.***

- Start two command windows, do an ssh session to woz in each window.
  - Open "man less" in one window.
  - Open "less moby.txt" in the other window.
  - Arrange the windows side by side.

There are a lot of less commands.  You don't need to learn them all immediately.  You don't need to learn some of them ever!

- How do you exit and get back to the terminal?
- Arrow keys and PgUp and PgDn keys work as expected.
- What key does half-page up?
- What key does half-page down?
- what do the space-bar and enter key when hit by themselves?
- What key by itself takes you to end of file?

### Numbers plus keys

- What does 50G do?
- What does 1G do?
- What does 50 plus spacebar do?  How is that different than spacebar by itself?
- What does the colon : do?

### Searching

- /*pattern*
  - n to go to next match
  - N to go to previous match
- ?*pattern* to search backwards
  - n to go to next match
  - N to go to previous match

## Manual pages

- Man pages are hated.  But they are useful.
- Attempted replacements
  - "info" pages
  - \-\-help
- Man pages persist
- A lot of times when you do a Google search on a command you just get links to the man pages.

## Movement

- q to quit.  This is important!
- man pages are displayed with less.  The less movement commands work in man pages.


## Man page of the man command

The man system is a system of documentation.  There are many sections.

For this course we will be concerned with Section 1 which is the default.  We may touch on a few others, but 1 is our goto section.

| Section | Content |
| :---: | :--- |
| 1 | Executable programs or shell commands |
| 2 | System calls (functions provided by the kernel) |
| 3 | Library calls (functions within program libraries) |
| 4 | Special files (usually found in /dev) |
| 5 | File formats and conventions eg /etc/passwd |
| 6 | Games |
| 7 | Miscellaneous (including macro packages and conventions), e.g. man(7), groff(7) |
| 8 | System administration commands (usually only for root) |
| 9 | Kernel routines [Non standard] |

Section numbers are given at the top of the page.

You can specify section numbers

```bash
$ man 1 ls
$ man 4 random
```q