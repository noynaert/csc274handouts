# Unit 11.040 If statements

## Review of original indentation

```bash
if [[ $A -eq $B ]]
  then echo "They are equal"
  else echo "They are not equal"
fi
```
## On a single line

If you want to do the command on a single line, then put a 
semicolon (;) at each new line.

```bash
if [[ $A -eq $B ]]```;``` then echo "They are equal"```;``` else echo "They are not equal"```;``` fi
```

## A compact arrangement

```bash
if [[ -d $FILENAME]]```;```then 
   echo "$FILENAME is a directory"
fi
```

## Else If

```elif```

```bash
if [[ -d $FILENAME ]]
  then echo "$FILENAME is a directory"
  elif [[ -f $FILENAME ]]
    then echo "$FILENAME is a regular file"
    else echo "$FILENAME is not a regular file or directory.  Maybe a link?"
fi
```
