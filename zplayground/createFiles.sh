#!/usr/bin/bash
items='01 02 03 04 05 06 07 08 09 10 11 12 25'
for i in $items; do
    fortune > "f$i.txt"
done
