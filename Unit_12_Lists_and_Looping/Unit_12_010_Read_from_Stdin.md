# Unit 12.010 Reading from Stdin

## ```read```

The ```read``` command reads from stdin and stores the value in a variable.

Create a realEcho file and make it executable.  

```bash
#!/usr/bin/bash
echo "Type something and press enter"
read SOMETHING
echo "$SOMETHING...$SOMETHING...$SOMETHING"
```

### An inline prompt

The -p option is used.  See the man page

Be sure to include a trailing blank space in order to make it look better.

```bash
#!/usr/bin/bash

read -p "Type something and hit ENTER " SOMETHING
echo "$SOMETHING...$SOMETHING...$SOMETHING"
```

### No prompt option

Technically no prompt is needed

The no-prompt option is most useful for filters

## A simple example

```bash
#!/usr/bin/bash
echo "Enter an integer"
read FIRST
read -p "Enter another number " SECOND
echo $(echo "$FIRST % $SECOND" | bc)

```
## Another way to prompt on the same line

### ```printf```

```bash
printf "Enter an integer "
read FIRST
```

## An example with error checking

```bash
#!/usr/bin/bash
echo "Enter an integer"
read FIRST
if [[ ! $(echo $FIRST | grep -E '^[+|-]?[0-9]+$') ]]
then
  echo "Must be an integer"
  exit 1  ## first integer is invalid
fi
read -p "Enter another number " SECOND
if [[ ! $(echo $SECOND | grep -E '^[+|-]?[0-9]+$') ]];then
  echo "Must be an integer"
  exit 2   # second parameter is invalid
fi
echo $(echo "$FIRST % $SECOND" | bc)
```