# Unit 07.020 vi

So far we have used ```nano``` and ```cat``` to create text files.

Nano is good for quick editing of short and simple text files, but it fails as an editor for programming.

## Practical issues of text editing

Teletype machines did not have "vertical scrolling." Editing text files (including programs) on teletype machines was forced to use "line editors." We put up with it because it was still better than punched cards

Dumb terminals allowed us to move the cursor up and down.  Line editors persisted for a while.

Also, dumb terminals did not have arrow keys.  Also no pgup, pgdown, home, or end.

vi became the established text editor.  It is part way between a line editor and a modern full screen GUI editor.

## ```vi``` and ```vim```

* vi  has largely been replaced by vim
  * vim takes advantage of modern displays and more powerful computers
  * vim uses color
  * multi-level undo
  * virtual mode (visually select text for copy/paste)
  * unicode support
  * lots of other stuff
* A lot of modern systems really use vim, even when you ask for vi
* vi has a steep learning curve
* vim is an extremely powerful editor once you master it.  It has ninja-level moves.
* Most modern IDEs for programming have vi/vim options
* A lot of the vi way of doing things is used in other places like ```less``` and man page navigation
  * So you already know some of the fairly sophisticated vi commands like searching
  * Run ```less``` on a file or bring up a man page.  See that colon at the bottom?  Get used to seeing it.

## Expectations for this course

* Be able to get in and out of vim
* Be able to insert and edit text
* Be able to undo
* Be able to search
* use the .vimrc file
* ***Not be intimidated by vim***

Things that are not required:

* Ninja-level vim skills
  * I'm OK with arrow keys instead of hjkl as arrows
* Actually liking vi.  At least not yet.

### Starting vi and vim

Usually either ```vi``` or ```vim``` followed by a file name.

When vi starts it is in "Command Mode"

To insert or edit text like you are used to, go into "Insert" mode

  * i takes you to insert mode.
  * There are about a thousand other ways, but i is what you will use most

### Moving Around in vi

* In command mode hjkl work as arrows
* Arrow keys work in both command and insert mode
* Mouse does not work!
  * Except in gvim or vim -g

### Exiting vi

Quiting involves leaving insert mode and going back into "Command" mode

* Esc key moves you into command mode
* If in doubt about which mode you are in, hit Esc twice

* ```:q``` quits
* ```:w``` writes out buffer to file
* ```wq``` writes and quits
* ```q!``` *read as "q bang" quits without saving


## Configuring vim

Hidden files that end in "rc" are usually configuration files.

.bashrc is configuration for bash
.profilerc is the configuration for profile
.vimrc is the configuration for vim

### A possible .vimrc file

```text
:set number
:syntax on
:set hlsearch
:set tabstop=4
:set autoindent
```