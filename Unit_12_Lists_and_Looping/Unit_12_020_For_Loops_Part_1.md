# Unit 11.020 ```for``` Loops and Lists

Bash for loops are similar to:

* for loops in Python
  
```python
for food in ["apples", "bananas", "green beans"]:
  print(x)  

for x in range(2, 30, 3):
  print(x)
```

* for .. in loops in Java

```java
String[] food = {"bananas", "apples", "green beans"};
for (String i : food) {
  System.out.println(i);
}
```

## Bash ```for``` loops

### ```for``` loop of a list

The simplest for loop is simply a list of strings

```bash
#!/usr/bin/bash
for FOOD in apple banana "green beans" avacado "brussels sprouts" kale
do
   echo $FOOD
done
```
This generates a list of strings with ```ls *.txt``` to produce a list of file names.  This also has a more involved body of the loop.

```bash
#!/usr/bin/bash
for FILE in $(ls *.txt)
do
  if [[ -f "$FILE" ]] ; then
   printf "The file is \"%s\" : " "$FILE"
   head -n 1 "$FILE" | tr "[a-z]" "[A-Z]"
   echo 
  fi
done
```

### A counting for loop

A counting loop may be simulated by using numbers.

```bash
for i in 1 3 5 7 9
do
   echo $i
done
```

Another way to do the counting loop is to use the ```seq``` command

```bash
for odd in $(seq 1 2 10)
do
        printf "%6.1f\n" $odd
done
```

Here is one more example using seq.  It is here mainly because computer scientists have an unnatural affection for modulo operations.  Try running this and notice that it produces a repeating cycle of 0, 1, 2, 3

```bash
for i in $(seq 0 20)
do
        printf "%2d\n" $(echo "$i % 5" | bc)
done
```
