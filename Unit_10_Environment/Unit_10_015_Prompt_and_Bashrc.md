# Unit 10.015 Prompt and Bashrc

$PS1 is a string that specifies your prompt

## Before we begin:

*** SAVE YOUR EXISTING PROMPT ***

```bash
PS1_ORIGINAL="$PS1"
```
## Prompt using simple text

```PS1="By Your Command > "```

### Does Unicode work?

* https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode
* https://getemoji.com/

## Prompt involving a character that must be escaped

```PS1="I am root \$ "```

## Basic Escape codes

* \a : an ASCII bell character (07)
* \d : the date in “Weekday Month Date” format (e.g., “Tue May 26”)
* \D{format} : the format is passed to strftime(3) and the result is inserted into the prompt string; an empty format results in a locale-specific time representation. The braces are required
* \e : an ASCII escape character (033)
* \h : the hostname up to the first ‘.’
* \H : the hostname
* \j : the number of jobs currently managed by the shell
* \l : the basename of the shell's terminal device name
* \n : newline
* \r : carriage return
* \s : the name of the shell, the basename of $0 (the portion following the final slash)
* \t : the current time in 24-hour HH:MM:SS format
* \T : the current time in 12-hour HH:MM:SS format
* \@ : the current time in 12-hour am/pm format
* \A : the current time in 24-hour HH:MM format
* \u : the username of the current user
* \v : the version of bash (e.g., 2.00)
* \V : the release of bash, version + patch level (e.g., 2.00.0)
* \w : the current working directory, with $HOME abbreviated with a tilde
* \W : the basename of the current working directory, with $HOME abbreviated with a tilde
* \\! : the history number of this command
* \\# : the command number of this command
* \\$ : if the effective UID is 0, a #, otherwise a $
* \nnn : the character corresponding to the octal number nnn
* \\\\ : a backslash
* \\[ : begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt
* \\] : end a sequence of non-printing characters

# Colors and more

## Reference for escape codes: 

* [https://misc.flogisoft.com/bash/tip_colors_and_formatting](https://misc.flogisoft.com/bash/tip_colors_and_formatting)

## Saving your PS1 in .bashrc

Saving the PS1 variable in .bashrc will preserve it through reboot

It is a variable, so it must be exported.

Why does this belong in .bashrc rather than in .profile?