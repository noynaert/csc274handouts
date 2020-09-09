# Unit_04_025_IO_Devices

* ```hexdump -C <filename>```


## Some Devices for stdout or stderr sinks

Some devices are oriented to being sources for stdin or sinks for stdout.  There are also some commands intended to be used with pipes

A good source for those who want to dig a little deeper is [https://unixbhaskar.wordpress.com/2010/09/15/exploring-devrandom-vs-devurandom-and-devzero-vs-devnull/](https://unixbhaskar.wordpress.com/2010/09/15/exploring-devrandom-vs-devurandom-and-devzero-vs-devnull/)

### ```/dev/null```

### ```/dev/zero```

### ```/dev/random``` and  ```/dev/urandom```

* /dev/random produces cryptographically robust random integer values.  
  * It draws from an "entropy pool" of system noise.  
  * If too many numbers are generated it can run out and will block.
  * More secure.  Best for protecting resources and cryptography
* /dev/urandom produces not quite as random variables, 
  * Will not block
  * Best for games or things that require a lot of random numbers
  * Probably secure for most cryptographic operations, but this is not certain.

#### Another alternative, the ```$RANDOM``` variable

It is not very random.  Probably good enough for wumpus-level games.

```bash
echo $RANDOM
cowsay $RANDOM
echo $RANDOM > mystery.txt


## Commands for piping or io

### ```echo```

### ```cat```

### ```yes```

### ```history```

## File that is useful

* /usr/share/dict/words