# Unit 10.020 Exit Codes, Falsiness, Truthiness

## Falsiness

---

> **falsiness**

> (computing, programming) The property of being falsy, i.e. evaluating to false in a Boolean context.

---
## **truthiness**

---

> **truthiness**

> (computing, programming) The property of being truthy, i.e. evaluating to false in a Boolean context.

---

***Anything that evaluates to 0 is false.  Anything that evaluates to non-zero is true***

Falsy Values | Truthy Values
---|---
false | true
0 | integers that are not 0
"" (Empty String)|"a" (String with length > 0)
Null or nothing|Something that isn't null or 0
Empty array or list|Array or list with at least one element
0| 0.0 (Effectively a string with length of 3)
A file does not exist | File exists
A file is empty | File has at least 1 character

## exit code

> ```$@``` is a variable that holds the exit code of the last command or function

Exit code is an integer from 0 through 255 (1 byte)

* Exit code of 0 is success
* Exit code of 1 through 255 is an error
  * Sometimes programs use specific numbers as error codes
  * The man page for many commands often have error codes near the end

A script ends with an  exit code.  The default is 0

The ```exit``` command can set the code.  Be sure to use it in a script, and not at the command line.  (In some ways the shell is one big script.)

### Meaning of the exit code

In some ways, exit codes are backwards from boolean.  To me it feels like success should be true and failure is false.  It may help to think of the exit code as an error number.  An error of 0 means no error occurred.