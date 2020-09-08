# Unit 04 Overview

## Unit Record Processing

The first commercial computer was produced in 1951.  But data processing using "Unit Record Processing" was done by businesses through the first half of the 20th century.  It was cumbersome in many ways, but amazing what could be done with it. [Unit Record Equipment](https://en.wikipedia.org/wiki/Unit_record_equipment)

It was done mostly with punched cards.  There were machines for punching cards, sorting them, tabulating them, and printing them.  They were well-made machines and were trusted by data processing staff.  [Here is a video about card sorters.](https://youtu.be/liXI4441j00).  If you have had a database course, then at 12 minutes you might catch something that looks like the predecessor of a "primary key" field. 

When IBM started making computers they needed input and output methods.  So they just adapted the unit record equipment everyone was comfortable using.  The unit record equipment was augmented by some computer hardware such as tape drives.  My high school had 2500 students, and in the late 1960s they were still using Unit Record Processing to process attendance and grades.  When I came to Missouri Western in 1985 the library was using a limited set of unit record equipment to keep track of checked out books.

## Unit Record Processing and Linux

My personal opinion is that Unit Record Processing had a lot of impacts on Unix.  In particular pipes seem like a variation on the workflow in unit record equipment. consider the following command. It replicates the flow from a deck of cards for students, runs them through a tabulating machine, and finally a printer.

```bash
cat students.txt | sort -d  | pr -n | lp -d OfficePrinter
```

## Strategy in this 
* Basic redirection
* Some common filters
  * Some Regex (Regular Expressions)
* More redirection

