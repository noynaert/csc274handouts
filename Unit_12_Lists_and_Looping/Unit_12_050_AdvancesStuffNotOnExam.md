# Unit 11.060 Advanced Stuff Not on the Test

## Case Statements

Bash has a case statement that is similar to switch and case statements in other languages.

The case statement is probably more important in bash scripts because it is used for processing command-line arguments.

[case statements](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html)

## Functions

There are build-in functions your scripts can use.  You may also write your own functions.

[Tutorial on Bash Functions](https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php)

## Arrays

Arrays look a lot like lists, but the syntax gets to be convoluted.  

### Declaring an array

```bash
FOODS=(apples oranges "green beans" banana)
```
But the complication comes in accessing the array.  It seems like ```echo $FOOD``` should print the list, but it only prints the first element.

To access anything except the first element, use the following bizarre syntax:
```echo ${FOOD[2]}```

There are two different ways to access the entire list.  

* ```${FOOD[*]}``` expands strings in quotes.  So "green" and "beans" would be 2 elements in the array
* ```${FOOD[@]}``` "green beans" would be a single element

## getopts()

The ```getopts``` function helps parse input parameters

Most programming languages such as Python have a getopt functions that do similar things

[getopt](https://sookocheff.com/post/bash/parsing-bash-script-arguments-with-shopts/)