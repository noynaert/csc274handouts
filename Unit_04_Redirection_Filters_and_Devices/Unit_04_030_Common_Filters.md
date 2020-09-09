# Unit 04_030 Common Filters

check out the folder /var/www/html/data.  What is the /var folder for?

Create a symbolic link to /var/www/html/data

```
ln -s  /var/www/html/data/fake data
ls
ls -l
```

## Notes on this unit

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

## ```cut```

```bash
cut -d ':' -f 2 data/real/mwsuLacross.csv
cut -d ':' -f 2,4 data/real/mwsuLacross.csv
```

# ```fold```

```bash
fold -w 20 data/real/mwsuLacross.csv
fold -sw 20 data/real/mwsuLacross.csv
```

## ```sort```

```bash
sort mwsuLacross.csv
sort -n mwsuLacross.csv
clear;sort -t ':' -k2 data/real/mwsuLacross.csv
```

## ```grep```

We are doing only simple patterns this week

### Flags to know
* ```-i```
* ```-w```
* ```-c```
* ```-n```
* ```-B```
* ```-C```
* ```-e```
* Working with multiple files
  * ```-r```
  * ```-l```
  * ```-L```

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

