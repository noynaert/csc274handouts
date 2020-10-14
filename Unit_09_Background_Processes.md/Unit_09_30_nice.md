# Unit 09.30 nice

## Performance

* Performance on a single user system
* Performance on a multi-user system
* Performance on a server

## Bottlenecks

Possible Bottlenecks in a computer system:

* Primary Storage (RAM, Memory)
* Secondary Storage (mainly disk access on modern systems)
* CPU

## The ```nice``` command is about CPU-bound processes

The ```nice``` command changes the priority for getting control of the CPU.

Niceness is a number between -20 and 19.

* Neutral niceness is 0
* Niceness of 1 through 19 acts nicely by giving others priority access to the cpu
* Negative niceness is in effect greedy.
  * Usually only the root user can create negative niceness

## Practical applications

```nice``` is not needed as often on modern systems

Still useful for computationally intensive applications

* Some theoretical problems with things like math and graph theory
* Some data analytics
  * But if the analytics are doing a lot of I/O, niceness does not matter much
* Some server applications to give good user response

