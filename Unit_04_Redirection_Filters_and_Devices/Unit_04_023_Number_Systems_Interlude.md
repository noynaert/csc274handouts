# Unit_04_023 Number Systems Interlude

## Some background on the nature of files and I/O devices

* ```hexdump -C <filename>```

### What are we looking at here?

We need to take a short dive into data representation.  

* Computer data in memory and on disk is stored as 0s and 1s.  This is the "binary number system."  We used the digital number system, based on powers of 10.

#### Decimal or Base 10

There are 10 digits, 0 through 9.  Note that in decimal we do not have a symbol for the concept of ten.  We use 10, which is 1 group of 10 plus 0.  

The decimal number 9876₁₀  could be described as 

9 thousands
8 hundreds
7 tens
6 ones
|9|8|7|6|
|:---:|:---:|:---:|:---:|
|10³ | 10² | 10¹ | 10⁰ |
|Thousand|Hundreds|Tens|Ones|
|position|position|position|position|

#### Octal or Base 8

There are 8 digits, 0 through 7.  Note that in Octal we do not have a symbol for the concept of 8.  We use 10₈, which is 1 group of 8 plus 0.  

The octal number 7654₈ could be represented as

|7 | 6 | 5 | 4 |
|:---:|:---:|:---:|:---:|
|8³ | 8² | 8¹ | 8⁰ |
|Five hundred and twelves|Sixty fours|Eights|Ones|
|position|position|position|position|

```
7 * 512 = 3584
6 *  64 =  384
5 *   8 =   40
4 *   1 =    4
```

So, 7654₈ would be equal to 4012₁₀

#### Binary or Base 2

There are 2 digits, 0 and 1.  Note that in Binary we do not have a symbol for the concept of two.  We use 10₂, which is 1 group of 2 plus 0.  

The binary number 1010₂ could be represented as

|1 | 0 | 1 | 1 |
|:---:|:---:|:---:|:---:|
|2³ | 2² | 2¹ | 2⁰ |
|Eights|Fours|Twos|Ones|
|position|position|position|position|

```
1 * 8 = 8
0 * 4 = 0
1 * 2 = 2
1 * 1 = 1
```

So, 1011₂ would be equal to 11₁₀ or B₁₆


#### Hexadecimal or hex or Base 16

There are 16 digits, 0 through F. (0,1,2,3,4,5,6,7,8,9,A,B,C,D,F)  Note that in hex we do not have a symbol for the concept of 16.  We use 10₁₆, which is 1 group of 16 plus 0.  

The hexadecimal number 89AB₁₆ could be represented as

|8 | 9 | A | B |
|:---:|:---:|:---:|:---:|
|16³ | 16² | 16¹ | 16⁰ |
|Four thousand ninety sixes|Two hundred fifty sixs | Sixteens|Ones|
|position|position|position|position|

```
8 * 4096 = 32768
9 *  256 =  2304
A *    8 =    80
B *    1 =    11
```

So, 89AB₁₆ would be equal to 35163₁₀

*The good news about hex is that we rarely are interested in converting anything over 15.*

### Counting in the different bases

#### A cheatsheet

 Decimal|Octal|Hex|Binary
 :---:|:---:|:---:|:---:
 0|0|0|0000
 1|1|1|0001
 2|2|2|0010
 3|3|3|0011
 4|4|4|0100
 5|5|5|0101
 6|6|6|0110
 7|7|7|0111
 8|10|8|1000
 9|11|9|1001
 10|12|A|1010
 11|13|B|1011
 12|14|C|1100
 13|15|D|1101
 14|16|E|1110
 15|17|F|1111
 16|20|10|10000
 
## ASCII Codes

Teletypes use 7-bit bytes.

2⁷ is 128.  If we start counting at 0, this allows values from 0 through 127.

## [ASCII Table](http://www.asciitable.com/)

Note that in the linked table, they do not bother to represent binary.  They don't need to because they have both octal and hex there.  Octal and Hex are both shorthand for Binary.

### ASCII CODES TO KNOW, but using 8 bits

**Know the first three columns**

Character|Decimal|Hex|Bit Pattern
:---:|:---:|:---:|:---:
Null or \0|0|00|0000 0000
CR or \n|13|D|0000 1101
space bar or [= =]|32|20|0010 0000
'0' (zero)|48|30|0011 0000
'@'|64|40|0100 0000
'A'|65|41|0100 0001
'a'|97|61|0110 0001
'~'|126|7E|0111 1110
&amp;nbsp;|255|FF|1111 1111

