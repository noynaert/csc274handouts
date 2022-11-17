# 09.40 nohup and disown

"HUP" means "Hang Up."  The SIGHUP signal is sent to jobs when the terminal session ends.  This means that all jobs started during the terminal session end when the terminal session ends.

There are several ways to "detach" a process from its terminal session.  One is ```hup``` and another is ```disown```

Modern computer systems are fast.  Frankly, there is less need of using hup and disown as well as background jobs in general.  It used to be a compile of a large C program could take hours.  It made a lot of sense to start a compile with nice and then take off to go eat dinner or do something else while the program compiled.  

It is not such a big deal now.  But there are still times when it is useful.  It may not be a daily event anymore, but it is common.

## First, we need something that isn't complicated, but will take a lot of time.  Here is a silly "Countdown" script I wrote:

```bash
#!/bin/bash
index=10   # sets a variable called "index"
echo "Counting down from $index"
sleep 1
while [ $index -ne 0 ] ; do
    echo "$index ..."
    sleep 1 
	index=$(($index-1))   # decrement $index
done
cowsay -f dragon-and-cow "Boom" | lolcat -h $(echo "$RANDOM % 10" | bc) -v 3
```
## ```nohup```

* ```nohup``` is usually run with & at the end to throw it into the background.
* Output is logged to file nohup.out
  * Other files may be specified
* The point is that you may now log out and the program will run to completion

You may want to remove nohup.out if it already exists.  It makes it easier to be sure the program actually ran.

## ```disown```

* Disown may be run on any job that is already in the background.
  * You may put it in background with & when you enter the command
  * You may put it in the background with ^Z
  * Does not automatically capture output.  If that is important use > to redirect the output when the command is launched.
  
