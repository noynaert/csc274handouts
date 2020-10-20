# Unit 10.020 Alias

Note: This section has nothing to do with [Jennifer Garner](https://en.wikipedia.org/wiki/Alias_(TV_series))

## ```alias```

The ```alias``` command lets you do a few things:

* see what aliases are already defined
* redefine how existing commands work
* create new commands

### See what aliases are defined

```alias``` by itself

```alias``` piped through grep

## Redefine how existing commands work

syntax:    ```alias new='command'```

* Do not put blanks around the replacement symbol(```=```)
* In most cases use single quotes rather than double

## Create new commands

Before you create a new command with alias, use the ```which``` command to make sure it is not using the same name

## ```unalias```

Unalias removes an alias.  If you run it during a session it removes the alias for the current session.  It will be back when you next log in.  (In the next section we will talk about how to remove it permanently.)

## Making aliases survive HUP

### Super sekret files

"rc" at the end of a file name usually means it is a configuration file.

Two hidden script-like files people confuse:

* **.profile** runs when you log in
* **.bashrc** starts before each bash session.

On woz almost everyone only logs in using bash.  So .profile runs first and then .bashrc runs.  If we were logging in and running a gui bash might not run at all unless we started a terminal session.  Or we could log in and use a different shell.  If we were runing th eborne shell or cshell then .bashrc would not run

To make commands available in every session, edit .bashrc and put the alias at the end of the file.

### Making ```unalias``` survive HUP

There are two situations:

* If the alias is in your own .bashrc either
  * delete the line
  * Put a # before the alias. This comments it out.  This is useful if you think you might want to put it back
* If it is a system-wide alias, use an unalias statement in your .bashrc