# Unit 07.70 Beginning Scripts

## $PATH

In unix, to execute a program or script, one of the two following things must be true:

* The file must be in a directory listed in the $PATH
* We must specify the directory and the file name

. is the current directory

## Super simple

* Just a text file with commands
* Current shell is assumed to be the language

```bash
figlet "Welcome $USER"
cowsay $(fortune)
```

### ```which```

### ShaBang

* The # key is known as the "sharp" key
* ! is bang

The "ShaBang must be on the first line and followed by the path to the command (determined by which)

```python
#!/usr/bin/python3

# determines if a number typed at the keyboard is even or odd

number = int(input ("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

## Cleanup with sed

* kill blank lines
* shorten variables

## the ~/bin folder

### check out .bashrc
