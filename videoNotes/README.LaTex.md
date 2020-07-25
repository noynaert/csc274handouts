# Compiling the notes

## Environment

I compiled the video notes on an Ubuntu 20.04 LTS System.

I used the following command to install LaTeX:

```bash
sudo apt install texlive-latex-extra
```

## Compiling

The source of the template recommended using pdflatex to compile the code.

I had to install the following packages to get the original template to compile.

```bash
sudo apt install texlive-science texlive-math-extra
sudo apt install texlive-lang-cyrillic
```
I think the cryrillic may be necessary because of some of the math in the original template.  You might not really need it for my pages.
