# Unit 04_030 Common Filters

check out the folder /var/www/html/data.  What is the /var folder for?

Create a symbolic link to /var/www/html/data

```
ln -s  /var/www/html/data/fake data
ls
ls -l
```

## Notes on this handout

Heavy reliance on man pages

Most Unix commands can either be run from either stdin or from an argument.  So the follwoing two commands are the same:

```bash
wc -l  data/docs/almaMater.txt 
cat data/docs/almaMater.txt | wc -l
```
or
```bash
cowsay 'Hello'
echo 'Hello' | cowsay
```

Generally, it is better to use arguments rather than cat or echo.  

* It is easier and shorter
* It is easier on system resources.  Cat'ing the file requires running cat as a command and opening an explicit pipe.  The argument handles it more efficiently.

So, in the following examples I will generally use arguments rather than filters.  However, when
we get into scripting we will often need to use pipes.

## ```wc```

If we always use only ASCII codes, then ```wc -c``` and ```wc -m``` should give the same results.  However, they do not if you use unicode.  (Run Unit_04_23 through wc with both -c and -m)

# ```fold```

```bash
fold -w 20 data/real/mwsuLacross.csv
fold -sw 20 data/real/mwsuLacross.csv
```


## ```cut```

```bash
cut -d ':' -f 2 data/real/mwsuLacross.csv
cut -d ':' -f 2,4 data/real/mwsuLacross.csv
cat /etc/passwd | cut -d: -f5
cat /etc/passwd | cut -d: -f1, 5
```

## ```grep```

We are doing only basic patterns for now  

Grep uses "regular expressions."

RE's are scary at first.  The key is to start small and easy

* In a regular expression, each character and digit matches itself.

### Flags to know
* ```-i``` Ignore case
* ```-w``` Whole Words only
* ```-c``` Count only
* ```-n``` Line Numbers
* ```-B``` Before
* ```-A``` After
* ```-C``` Context
* ```-e``` "Extended"
* ```-v``` Invert selection
 
  
* Working with multiple files
  * ```-r``` Recursive
  * ```-l``` Files with matches
  * ```-L``` Files without match

Forms of regular expressions

* BRE -- Basic Regular Expressions
* ERE -- Extended Regular Expressions
* PCRE -- Perl Regular Expressions (also Python and Java, but it doesn't play nicely with Java syntax)

See the man page and search for "Character Classes and Bracket Expressions" for more information.

* Letters, digits, and some special characters match themselves
* Bracket [ ] expressions
* ^ start of line
* $ end of line
* Character Classes to know:
  * [:alnum:]
  * [:alpha:]
  * [:cntrl:]
  * [:digit:]
  * [:graph:]
  * [:lower:]
  * [:print:]
  * [:punct:]
  * [:space:]
  * [:upper:]
  * [:xdigit:]
* Repetitions
  *  ? The preceding item is optional and matched at most once.
  *  * The preceding item will be matched zero or more times.
  *  +      The preceding item will be matched one or more times.
  *  {n}    The preceding item is matched exactly n times.
  *  {n,}   The preceding item is matched n or more times.
  *  {,m}   The preceding item is matched at most m times.  This  is  a  GNU extension.
  *  {n,m}  The  preceding  item  is  matched at least n times, but not more than m times.


Examples

```bash
grep  "some.*" /usr/share/dict/words
grep  "some.*" /usr/share/dict/words | less
grep -we "some.*" /usr/share/dict/words | less
grep -we "some.*" /usr/share/dict/words | less
grep -wce "some.*" /usr/share/dict/words 
grep -wrce "some.*" /usr/share/dict/
grep -r 'Mark Twain' data
grep -rl 'Mark Twain' data
```

## ```egrep```

Same as grep -e

## ```sort```

```bash
sort mwsuLacross.csv
sort -n mwsuLacross.csv
clear;sort -t ':' -k2 data/real/mwsuLacross.csv
```

* ```-n``` numeric
* ```-f``` ignore case
* ```-R``` random
* ```-r``` reverse the comparison (take the compliment)
* ```-k``` key (KEYDEF simple form is just the field number)
* ```-t``` field separator (use with -k if the field separator is not whitespace)


## ```tr```

* Very simple translator for streams
* I suggest putting set1 and set2 in single quotes

```bash
tr 'AEIOU' 'aeiou' < data/real/mwsuLacross.csv
tr 'A-Z' 'a-z' < data/real/mwsuLacross.csv
tr '[:upper:]' '[:lower:]' < data/real/mwsuLacross.csv
tr '[:digit:]' '+' < data/real/mwsuLacross.csv
tr ':' '|' < data/real/mwsuLacross.csv
```

## ```sed```

Sed is a full language, but it is often used at the command line.  In my experience, the two most common things to do with it are to do global search and replace or to delete lines.

The BSD and Linux versions of sed are a little different.  

* A big difference: the BSD version actually changes the file.  
* The Linux system just sends data to stdout.  You may either:
  * Redirect the output to a new file
  * Use the -i option to alter the file 

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

```awk``` is another very useful command line filter.  It is similar to SED and tr.  But AWK is really oriented to manipulating data.  It also lays the groundwork for some advanced regular expression processing (including in Python).  

This is a good video on [Gary Explains, EVERYONE Nees to Learn a Little Bit of AWK!](https://youtu.be/jJ02kEETw70).  You only need to watch up to the 6:00 mark when the add starts. That is also where the commercial starts. The material after that is excellent, but goes beyond the survey-nature of this course.  Also, we will be doing some of the material after the commercial later in the class. I will probably link to the end material there.

To some extent some awk actions can be done in R, but awk still has an important role.
