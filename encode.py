#!/usr/bin/python3

## programming convention:
# I know "camel case" is a C codeing convention, but I like it!
# so please capitaliz the second word of a variable
# so Nathan's House as a variable would become: nathansHouse

#First we import some libraries. These will include additional functions that we need.
import math
import time
import random
import fileinput

# Next I want to define Variables. Strictly speaking we dont have to do this in Python
# However, this is common in C programming and I really like it, it gives me an easy place to 
# look to remember all my variables

transmitLetter = ""
transmitTime = 0
transmitCount = 0
uncodedMessage = ""

def main():
	encode();

def encode():
	for letter in fileinput.input():
		print (letter)
	
main();

