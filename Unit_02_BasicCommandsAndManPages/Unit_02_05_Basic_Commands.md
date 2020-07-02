# Unit 02_05, Basic Commands

Make sure you have a terminal window open.

## The Prompt

## Typing Commands

* Commands are *case sensitive.*
  * Most commands are all lower case
* Some simple commands to try:
  * date
  * cal
  * clear
  * pwd
  * fortune (this may not be installed on all systems)

## Istalling new commands

Three main types of distributions
* Debian Based  (.deb)
  * Debian
  * Ubuntu, Kubuntu, etc
  * Mint
  * Pop!
* Red Hat (.rpm based)
  * Red Hat
  * Fedora
  * Suse
* Others
  * Arch
  * Slackware
  
### Apt  
  * apt or apt-get for .deb distributions
  * dnf or yum for .rpm distributions

### New kids on the block:
  * snap
  * flatpack
  * appimagec      

## Arguments, Flags, and Options

Some commands have arguments, flags, or options after them.

### Arguments

Arguments are often some type of text that a command operates on.

```bash
echo Pizza
cal 2024
cal 2 2028
```

Sometimes arguments have more than one word.

White space separates arguments.  (Whitespace is the space bar, tab key, Enter key, and a few others that are rare.)

If there are multiple white spaces together, the white space is collapsed.  If you know HTML you are probably familiar with this.

So, if you put in odd spacing, it will get collapsed into a single space

```bash
echo Pepperoni           Pizza
```

You may use "double quotes" to force the white space to be honored.

```bash
echo "Pepperoni           Pizza"
```

'Single quotes' work, too.  But they mean something slightly different.  For now, just use double quotes

```bash
echo 'Pepperoni           Pizza'
```

#### cowsay

Cowsay is like echo, but with a cow.  (You might have to install it)

```bash
cowsay Pepperoni           Pizza
```

### Flags

Flags change something about the way the command operates.  A flag is usually a - followed by a letter (There is also sometimes a long form that uses two dashes, but we will cover those later.)

To get a dead cow, try ```cowsay -d "uh-oh"```  or to get a wired cow try ```cowsay -w "Too much coffee"```

### Option

An argument is similar to a flag, but an option takes an extra bit of information.

In the following, -f is an option that requires a file name.  

```bash
cowsay -f tux "Hi"
```

Actually, the space between the option and the argument is optional, so the following would also work.  But the space makes things more readable.

```bash
cowsay -ftux "Hi"
```

## Don't worry about too many details at this point

There are actually fairly complex rules about when you can and can't use blanks, what happens which flags conflict, and other factors.  For example, what would happen if you asked for a cow that was both wired and dead?  The important thing for now is to not sweat the details too much.  For now, get comfortable entering commands.  Get used to editing them with the arrow keys and backspace.  You can worry about the minutia of syntax later.

As always, 

```bash
cowsay -f dragon "Have a lot of fun!"
```
