# Unit 10.1 Bash variables

* Bash variables are similar to variables in programming languages
* Variables are created when they are assigned a value.  The assignment character is =
* There is no type associated with the variable.  They are technically strings, but may be converted to numbers if appropriate
* $ use
  * They do not start with a $ when on the left side of an assignment statement
  * To reference the variable they must have a $ in front of them
* Traditionally they are in ALL CAPS but do not have to be.


## ```env```

By itself the ```env``` command produces a list of shell variables that are set

### some examples

```bash
env
echo $USER
echo $PWD
WELCOME="Hello $USER"
cowsay $WELCOME
NOW="$(date)"
echo $NOW
USER_COUNT="$(finger | wc -l)"
echo $USER_COUNT
echo $PS1
PS1_ORIGINAL=$PS1
PS1="> "
PS1="Howdy >"
PS1=$PS1_ORIGINAL
```

## Variables in Scripts

Scripts can access the variables created in the shell.

Scripts are like Vegas.  By default, *variables created in a script stay in the script.* Child processes do not inherit the variables.

Here is a script I call askTux

```bash
#!/usr/bin/bash
cowsay -ftux "The number is $NUMBER."
```

Now try the following:

```bash
NUMBER=42
./asktux
```

```bash
NUMBER=88
./asktux
export NUMBER
./asktux
```