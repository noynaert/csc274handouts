# Uni_04.40 More Redirection

These are some tools we will use more as we move into scripting

## tee

Sends output to two places:

1. stdout
2. The specified file

* Usually used as the tail end of a pipe.
* To document everything run a bash shell and pipe it through tee.

-a is probably the most common flag.  It appends to a file and does not replace it.

Good for documenting what you are doing on the system

## HERE operations and HERE documents

Used for multi-line input

The operator is << followed by an ID of your choice.

Then there is a multi-line input

End the input by putting the ID at the beginning of the next line.

There is no interpolation or expansion of anything in the string.

## $() operations

Allows you to use a command within another command

You can put a system command in the () and it will execute.

```bash
    cowsay $(ls -a)
```
