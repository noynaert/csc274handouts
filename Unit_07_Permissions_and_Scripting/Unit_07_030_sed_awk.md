## ```sed```

```sed``` does much the same thing as the ```tr``` command, but on steroids

* tr allows matching single characters.  sed uses matching on regular expressions
* tr only allows the substitution of characters.  sed allows changing the number of characters
* sed does a lot of other things like delete lines
* tr is a lot faster if you only need to change single characters

Sed is a full language, but it is often used at the command line.  In my experience, the two most common things to do with it are to do global search and replace or to delete lines.

The sed syntax shows up in a lot of other places.

The BSD and Linux versions of sed are a little different.  

* A big difference: the BSD version actually changes the file.  
* The Linux system just sends data to stdout.  You may either:
  * Redirect the output to a new file
  * Use the -i option to alter the file 
  * A lot of people ```cat``` data files into sed.  This protects you from accidentally changing the file if your system is set up to use the -i option by default.

At the command line we usually have some pattern to match.  We are mostly doing simple patterns in this unit, but they can be complex.

* ```sed 's/pattern/result/i'``` would replace all occurrences of pattern with result in the stdin stream or file
* ```sed '/pattern/d' ``` would delete lines with the pattern in it.

```bash
sed 's/Missouri/Missourah/gi' data/docs/almaMater.txt # changes Missouri to Missourah 
sed '/Missouri/d' data/docs/almaMater.txt # deletes lines with Missouri
sed '/^$/d' data/docs/almaMater.txt  # ^ is a pattern that indicates beginning of line
                                     # $ is a pattern that indicates end of line
```

Good lesson at [https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux](https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux)

[TutorialsPoint](https://www.tutorialspoint.com/sed/sed_workflow.htm) has a tutorial that shows what goes on internally.  It is really good if you become a heavy user and need to understand behind the scenes.

## ```awk```

```awk``` is another very useful command line filter.  Awk is a version
of the ```cut`` command on steroids.   

* Both cut and awk allow you to extract fields
* awk allows selection by regular expressions rather than just field delimiters.
* awk gives more formatting control of output
* awk can do arithmetic and functions 
* awk is a programming language
* cut is a lot faster when it will do.

This is a good video on [Gary Explains, EVERYONE Needs to Learn a Little Bit of AWK!](https://youtu.be/jJ02kEETw70).  You only need to watch up to the 6:00 mark when the ad starts. That is also where the commercial starts. The material after that is excellent, but goes beyond the survey-nature of this course.  Also, we will be doing some of the material after the commercial later in the class. I will probably link to the end material there.

To some extent some awk actions can be done in R, but awk still has an important role.