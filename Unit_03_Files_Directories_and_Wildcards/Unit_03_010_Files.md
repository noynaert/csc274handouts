# Unit 03  Files

## A couple of commands we will use a lot in this unit

### ```ls```

* ```ls``` is going to be our main command for this page.
* Check out the man page
* Flags we will be using the most -a and -l, or -al

### Reading output from ```ls -al```

```bash
[abyron@woz ~]$ ls
dilbert.cow  moby.txt
[abyron@woz ~]$ ls -l
total 1192
-rw-rw-r--. 1 abyron abyron    2050 Aug 21 08:25 dilbert.cow
-rw-rw-r--. 1 abyron abyron 1214557 Jun 17  2019 moby.txt
```

* column 1 ```-rw-rw-r--.```
  * The first character is the file type.
    * - is a regular file
    * d is a directory
    * l is a link
    * c is a character device
    * b is a block device, usually a disk or secondary storage
    * s is a socket
    * p is a named pipe
  * ```rw-rw-r--``` are the file permissions.  In this case the owner can read and write the file, but not execute it.  The primary group is the same, and anyone in the world can read the file, but not write to it or execute it.
* Second column 
  * The number is the number of links pointing to the file.  Actually, it is only the number of "hard links."  
* columns 3 and 4
  * This is the owner and primary group for the file.
* column 5 is the size of the file in bytes
* column 6 is the last modified date
  * change the date to right now with the ```touch``` command
* column 7 
  * Name of the file, except for links
  * For links it is the local name -> and the name of the file linked to.
  * ```csc274videonotes.sty -> ../unit00/csc274videonotes.sty```




### ```cat```

```cat``` is short for "concatinate"  Technically it is for combining two or more files.  Its common use is to list a single file to the console.  ```less``` is often a better alternative if you actually want to read the file.

## What is a file?

* In Unix, all data is organized into files
* All files have a name
* The common saying is "In Unix everything is a file."
  * Some things that would not be files in other OS are in Unix
  
  ```bash
  ls /proc
  ls -l /proc | less
  cat /proc/cpuinfo | less
  cat /proc/meminfo | less
  ls -l /dev | less
  ```

## File Names

For reference on file names: [https://www.cyberciti.biz/faq/linuxunix-rules-for-naming-file-and-directory-names/](https://www.cyberciti.biz/faq/linuxunix-rules-for-naming-file-and-directory-names/)

* Blanks are allowed, but do not use them if you can help it.  Also avoid special characters like & and |.
* **File names that start with a period are *hidden* files.** You probably have a lot of hidden files in your root directory.  
  * ```ls -a``` and ```ls -al```
* Two special file names (actually, directory names)
  * . "dot" the current directory
  * .. "double dot" the parent directory

## File Types

* Normal Files
* Normal Directories
* Special Files
  * Links
  * Sockets
  * Named Pipes
  * Block Devices

## Links

* Hard Links
* Symbollic Links

Links are placeholders that point to other files.  The link acts just like it is the original file, but it is actually in a different location. In practice most links are symbollic links

### Other Special file types

There are other file types such as sockets and named pipes.  They are beyond what we are doing in this class.  [Here is a link to an article that briefly explores the various types.](https://www.tecmint.com/explanation-of-everything-is-a-file-and-types-of-files-in-linux/)

## Commands for files

* ```touch``` 
  * Updates a file's last modified date
  * Also often used to create an empty file
* ```cat```
  * Technically it is used to join two or more files into a single file.
  * Often it is used to list the contents of a text file to the console
* ```less``` Better than cat on modern consoles.  Also better than ```more```
* ```head``` and ```tail```
  * tail -f 
  * Lists the first or last lines of a file.
* ```cp``` 
  * Copies a file.  
  * Always takes two arguments.  It uses the "from to" sequence for the arguments. or "source destination"
    * Second argument is the new file name *or* the directory where the file is to be placed
    * If you are copying from a different directory and want to keep the same file name, use . as the directory name.  *This is very common.*
* ```rm``` removes the file
* ```mv``` 
  * Technically it is used to move a file to a different directory
  * Most of the time it is used to rename a file or directory

### Non-Roman alphabets

Unix was written using ASCII.  Linux was adapted to handle extended ASCII.  Now it generally supports other alphabets

## Editing text files

* ```nano```  Nano is a simple text editor.  It is easy but very limited in its abilities.  Most versions of Linux have it as an emergency tool for people who don't know vi or vim.
* ```vi```, ```vim``` 
  * These are much more powerful editors.  
  * Unfortunately they are modal editors and have a steep learning curve.  
  * vi is the traditional editor for Unix systems.  vim is an upgraded version that works with colors and other things that were not available on teletypes and dumb terminals.  If you have a choice, always opt for vim.
  * vi and vim commands run throughout Linux and Unix.  For example, the controls used in ```more``` and ```less``` are actually commands from vi and vim.  
