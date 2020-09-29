#!/usr/bin/python3

# determines if a number typed at the keyboard is even or odd

number = int(input ("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
