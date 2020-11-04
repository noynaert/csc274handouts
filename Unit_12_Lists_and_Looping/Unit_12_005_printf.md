# Unit 12.005 ```printf```

## ```echo``` 

* simple
* no formatting
* automatically puts on a \n (new line)
* does not store to a variable, but there isn't much to store

## ```printf```

* more complicated, but more powerful
* allows formatting using C-style printf
* does not automatically put in a new line
* has option to store the output to a variable

### A few format specifiers

Specifier|Meaning
:---:|---
\n|New Line
%d|Integer (as decimal)
%x|Integer (as hexadecimal)
%f|Floating Point
%s|String

```bash
$ printf "%d\n" 42
42

$ printf "%f\n" 42
42.000000

$ printf "%s\n" 42
42

$ printf "%x\n" 42
2a

$ printf "Vegetables: %d  Fruits %d\n" 14 8
Vegetables: 14  Fruits 8

$ printf "Vegetables: %d\nFruits %d\n" 14 8
Vegetables: 14
Fruits 8
```

## Assigning formatted data to a variable

```bash
$ PI=$(printf "%3.2f" 3.14159)
$ echo $PI
3.14
```
