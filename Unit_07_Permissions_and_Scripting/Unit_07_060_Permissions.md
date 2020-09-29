# Unit 07 060 File and Directory Permissions

```bash
ls -l evenOrOdd.py
```
Result:

```text
   -rw-rw-r-- 1 noynaert noynaert  212 Sep 29 00:03 evenOrOdd.py
```
The critical part for this page is **rw-rw-r--**

This is three groups of 3 characters.

* Each triplet of 3 is for Read, Write, Execute
* Triplets:
  * First triplet is for the user
  * Second triplet is for the group
  * Third triplet is for the world (all users)

Execute on a directory means "permission to read"

## ```chmod```

## chmod is used to change permissions

### The old way

3 bits are an octal (base 8) number system

rwe|bits|octal
---|---|---
---|000|0
--e|001|1
-w-|010|2
-we|011|3
r--|100|4
r-e|101|5
rw-|110|6
rwe|700|7

* In practice, 0, 4, 6, and 7 are the most common
* "write" implies ability to rename or delete
* Modern unix systems create a primary group for every user.

```bash
chmod 700 evenOrOdd.py
chmod 777 evenOrOdd.py
chmod 500 evenOrOdd.py
chmod 000 evenOrOdd.py
```

### Another way

The permissions may be changed one at a time using + or - notation.

```bash
chmod u+x evenOrOdd.py # give the user execute permission
chmod a-x evenOrOdd.py # take away the user execute permission