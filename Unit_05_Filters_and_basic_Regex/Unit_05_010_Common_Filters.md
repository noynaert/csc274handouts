# Unit 05_010 Common Filters

check out the folder /var/www/html/data.  What is the /var folder for?

Create a symbolic link to /var/www/html/data

```
ln -s  /var/www/html/data data
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

## ```fold```

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
 
## ```grep```

Grep uses "regular expressions."

RE's are scary at first.  The key is to start small and easy

We are doing only basic patterns for now  

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
* ```.``` any single character
* ^ start of line
* $ end of line
* Character Classes to know:
  * [[:alnum:]] or \w    \W is anything that is not alnum
  * [[:alpha:]]
  * [[:cntrl:]]
  * [[:digit:]]
  * [[:graph:]]
  * [[:lower:]]
  * [[:print:]]
  * [[:punct:]]
  * [[:space:]]
  * [[:upper:]]
  * [[:xdigit:]]
* Repetitions
  * ```*``` Zero or more of the previous character
  *  ```?``` The preceding item is optional and matched at most once.
  *  ```{n}```    The preceding item is matched exactly n times.
  *  ```{n,}```   The preceding item is matched n or more times.
  *  ```{,m}```   The preceding item is matched at most m times.  This  is  a  GNU extension.
  *  ```{n,m}```  The  preceding  item  is  matched at least n times, but not more than m times.


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



