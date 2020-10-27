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

Scripts may create and use their own variables.

Here is a script that sets a variable to a random value from 1 through 10 and prints it to stdout.  I will call it 1to10

```bash
    #!/usr/bin/bash
    NUMBER=echo "$RANDOM % 10 + 1" | bc
    echo $NUMBER
```

Scripts are like Vegas.  By default, *variables created in a script stay in the script.* Child processes do not inherit the variables.

Here is a script I call askTux

```bash
#!/usr/bin/bash
cowsay -ftux "The number is $NUMBER."
```

Add the following line to the end of the 1to10 script.

```bash
   ./askTux
```
In this case 1to10 is the parent.  askTux is the child.  By default the parent is not passed to the child.

### export

If a child needs the variable, it must be exported.

Export may be done as a separate step

```bash
    #!/usr/bin/bash
    NUMBER=$(echo "$RANDOM % 10 + 1" | bc)
    export NUMBER
    echo $NUMBER
    ./askTux
```
export NUMBER
./asktux
```

Another way is to export it at the time it is created:

```bash
export NUMBER=$(echo "$RANDOM % 10 + 1" | bc)
./asktux
```

## Exporting from the shell

When a script is called from the command line the shell is the parent and the script is the child.  The shell must export the variable.