# Unit 04_030 Common Filters

check out the folder /var/www/html/data.  What is the /var folder for?

Create a symbolic link to /var/www/html/data

```
ln -s  /var/www/html/data/fake data
ls
ls -l
```

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
```

## ```egrep```

Same as grep -e

## ```tr```

## ```sed```

Good lesson at [https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux](https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux)

## pr

## print

