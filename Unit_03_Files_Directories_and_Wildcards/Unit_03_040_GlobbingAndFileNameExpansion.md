# Globbing and File Name expansion

## Building our playground

These commands may be used to start building our playground:

```bash
wget http://woz.cs.missouriwestern.edu/playground.tar.gz
ls
tar -xzvf playground.tar.gz
ls
cd playground
pwd
```

## File name completion

The Tab key is your friend.  If you type the first part of a file name and the name is unique bash will complete the name for you

Go into your playground folder if you are not already there. Try typing the following, but press the Tab key in place of the ⇄ symbol

```
ls -l mob⇄
```
If there is are multiple file that match, hitting the tab key twice will show you.  Try ```ls -l m⇄```  There is an ambiguity, so hit the Tab key a second time to see your options.

## Asterisk *

Asterisk means match zero or more characters
