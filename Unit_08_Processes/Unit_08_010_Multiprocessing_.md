# Unit 08.010 Multiprocessing

## CPU

The processor is the "brains" of the computer.  In classic computer design the Central Processing Unit does the calculation and logic involved in running the entire computer system.

Historically there has been one CPU for the computer.  Things have changed.

* Computers now have multiple "cores" or processors.
  * "Quad core" (4 CPUs on a single chip) is now the minimum for laptops and PCs
  * A lot of the computation and logic that used to be done on the CPU has been offloaded
    * Graphics cards
    * IO devices and I/O buses on the motherboard keep getting smarter


## Multiprocessing

A computer with only 1 CPU can only run one program at a time.  Multiprocessing systems give the *illusion* of having multiple processors by switching the CPU rapidly between programs.  CSC 386, Operating Systems, explores how this is done.

When there are multiple cores (processors) the problem is similar.  Except instead of switching a single CPU the operating system must switch programs between multiple cores.  

## CPU Information

* CPU information is in /proc/cpuinfo
  * Remember that this is treated like it is a file, so ```cat``` works with it
  * Grep is your friend.  Other utilities can help as well.

The following script prints CPU information.  
  * # indicates the start of a comment.  The rest of the line after the # is all comment.
  * \ may be used when it is necessary or desirable to "wrap" a command to the next line.
```bash
#!/usr/bin/bash
# Prints vendor, model name, and core count
echo "CPU Information"
echo "  Vendor: $(cat /proc/cpuinfo | grep vendor | uniq)"
echo "  $(cat /proc/cpuinfo | grep 'model name' | uniq | \
sed 's/model name/Model Name/')"
echo "  Processor Count: $(cat /proc/cpuinfo | grep 'processor' | wc -l)"
```
The ```lscpu``` command produces a summary of the plethora of information in /proc/cpuinfo.  Note that lscpu is a command, not a file.
