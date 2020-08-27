# Unit 03  Globbing and vi

## ```ls```

* ```ls``` is going to be our main command for this page.
* Check out the man page
* Flags we will be using the most -a and -l, or -al
## What is a file?

* In Unix, all data is organized into files
* All files have a name
* The common saying is "In Unix everything is a file."
  * Some things that would not be files in other OS are in Unix
  
  ```bash
  ls /proc
  cat /proc/cpuinfo | less
  cat /proc/meminfo | less
  ```

## File Names

For reference on file names: [https://www.cyberciti.biz/faq/linuxunix-rules-for-naming-file-and-directory-names/](https://www.cyberciti.biz/faq/linuxunix-rules-for-naming-file-and-directory-names/)

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


## Going further

### Other Special file types

There are other file types such as sockets and named pipes.  They are beyond what we are doing in this class.  [Here is a link to an article that briefly explores the various types.](https://www.tecmint.com/explanation-of-everything-is-a-file-and-types-of-files-in-linux/)

### Non-Roman alphabets

Unix was written using ASCII.  Linux was adapted to handle extended ASCII.  Now it generally supports other alphabets

