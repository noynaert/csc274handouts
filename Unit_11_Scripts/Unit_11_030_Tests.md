# Unit 11.030 Tests

I will list some of the most important and frequently used tests.  A more complete list is in ```man test```.

## flags

* -n  String has at least 1 character ```if [[ -n $1 ]]```
* -z  String has zero length
* -e  A file exists ```if [[ -e abc.txt ]]```
* -f  A file exists and is a regular file ```if [[ -e abc.txt ]]```
* -d  A file exists and is a directory ```if [[ -e abc.txt ]]```
 
 ## strings

 = and == mean the same thing.  The item on the right may be a regular expression

 The following operators should only be used with strings and not integers.

 * = or ==
 * !=
 * &gt;
 * &lt;
 * &gt;=
 * &lt;=
 * =~  (regular expression)

## integers

* -eq
* -ne
* -lt
* -le
* -gt
* -ge

## boolean operators

* ! not
* || or
* && and
  
  There are also -a and -o commands for and and or