# Globbing and File Name expansion

## Building our playground

These commands may be used to start building our playground:

```bash
wget http://woz.csmp.missouriwestern.edu/playground.tar.gz
ls
tar -xzvf playground.tar.gz
ls
cd playground
pwd
```

## File name completion

The Tab key is your friend. If you type the first part of a file name and the name is unique bash will complete the name for you

Go into your playground folder if you are not already there. Try typing the following, but press the Tab key in place of the ⇄ symbol

```
ls -l mob⇄
```

If there is are multiple file that match, hitting the tab key twice will show you. Try `ls -l m⇄` There is an ambiguity, so hit the Tab key a second time to see your options.

## Asterisk \*

Asterisk means match zero or more characters

This is the most permissive, and also the most widely used wildcard character.

`\*.txt` would match any file ending in .txt

## Question Marks ?

The Question Mark matches one character.

## Square Brackets [ ]

Square Brackets give us a list of characters to pick from.

`[mq]*` would select all files starting with either an m or a q.

We can also specify a range

`f[0-9]*` would select all of the files starting with f followed by a digit.

`f[a-zA-Z]*` would select all of the files starting with f that had a letter follow the f.
