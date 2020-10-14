# Unit 09.020 Jobs 

## ```fg```

```fg``` is a built-in command.  It moves a job from background to foreground

### ```job```

A "job" is a process that was launched from a terminal and is now in the background.

```jobs``` is a built-in command that shows all the jobs.

```text
[abyron@woz ~]$ jobs
[1]   Running                 xeyes &
[2]   Running                 xclock &
[3]-  Stopped                 sl
[4]   Running                 xterm &
[5]+  Stopped                 sl
```

```fg %3``` would move the top sl to the foreground



nohup