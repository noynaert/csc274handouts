# Unit 03 020 Directories

* Directories are just a special type of file
* Directories may contain files *and other directories*
* Microsoft and directory structures
  * MS-DOS version 1 did not have directories
  * MS-DOS version 2 adopted the Unix system pretty much directly
    * They had to reverse the direction of the /
    * They had aliases for some of the directory manipulation commands.  Ironically, they made their own new commands more Unix-like.
  * On Windows 95 and later systems, Microsoft uses "folders" to be more user friendly, but they mean exactly the same thing.

## Separator is / on *nix systems

## Recursive

On unix when a directory command is *recursive* it means it applies to all directories below the named directory

Recursive operations are often indicated by an ```-r``` flag.  Sometimes it is ```-R``` or ```--Recursive``` if -r is already used for something else.

When you use ls on a directory name, it automatically lists the contents of the directory (technically not fully recursive).  To get the names of directories use ```ls -d```

## Directory commands

* pwd
* cd
  * cd ..
  * cd .  (Why is this a rather pointless thing to do?)
* mkdir (md on MS-DOS and Windows)
* rmdir (rm on MS-DOS and Windows)
* rm -r  Really a file command, but when you add the -r it goes "recursive" and works on directories

## Paths

### Relative Path

A relative path starts in the current directory, or from a . or .. 

A command that uses a relative command in one directory is may give different results if used from a different directory

### Absolute Path

Starts with the "Root" /

Should work the same from anywhere on the system

### ```~```

Tilde is the home directory of the user

It is usually the same as /home/$USER but not always.

