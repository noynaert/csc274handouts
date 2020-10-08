# Unit 08.20 "Memory"

## RAM, "Primary Storage,"Memory"

* A program must be loaded into RAM in order to run
* SWAP
  * Swap is an overflow area for RAM.  If RAM is full, the extra data goes to swap.
  * Swap is on the hard drive
    * The hard drive is roughly a thousand to a million times slower than Primary Storage
    * "Thrashing" is when material is being moved back and forth constantly between primary storage and swap space

### Measuring RAM (and other stuff)

Two definitions of a byte (for modern computers):
* A byte is the amount of space needed to hold 1 ASCII character.  
* A byte is 8 bits.  

Why do both of the above mean the same thing (if you use extended ASCII)?
     
Number of Bytes|Prefix| English Approximation|Power of 2|Amount of Data
---|---|---|---|---
1,024| Kilobye | Thousand | 2¹⁰ |A paragraph of text
1,048,576| Megabye | Million | 2²⁰ |A small novel
1,073,741,824| Gigabyte | Billion | 2³⁰ |Beethoven's 5th symphony (as music)
1.0995116e+12| Terabyte | Trillion | 2⁴⁰ |All the xrays in a large hospital (as images)
1.1258999e+15| Petabyte | Quadrillion | 2⁵⁰ |Contents of all US academic research libraries as text



