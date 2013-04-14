#!/usr/bin/python3

## programming convention:
# I know "camel case" is a C codeing convention, but I like it!
# so please capitaliz the second word of a variable
# so Nathan's House as a variable would become: nathansHouse

## Transit string:
# as of now the tranmsited message (encodedMessage) is sent as follows:
# date,time,randomNumber, letter, letter, ................

#First we import some libraries. These will include additional functions that we need.
import math
import time
import random
import os
import sys
from optparse import OptionParser

# a quick definition
encodedMessage = ""
global fileName
dryRun = 0
outputFile = "output.txt"



# the parser is a better way to read command line arguments!
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE", action="store", type="string")
parser.add_option("-v", "--verbose", action="count", dest="verbosity", help="print output", default=0)  
parser.add_option("-d", "--dry-run", action="count", dest="dryrun", help="same as verbose with no output file", default=0)  
parser.add_option("-o", "--output", dest="outfile", help="specify output FILE", metavar="FILE", action="store", type="string", default="output.txt")  
(options, args) = parser.parse_args()
fileName = options.filename
verbosity = options.verbosity
outputFile = options.outfile
dryRun = options.dryrun
if dryRun > 0:
	verbosity = 1
if not options.filename: 
    parser.error("You must specify an input file")


# we are going to create a main function, this will be important later, when we need to decide if we are encoding or decoding
def main():
	makeTime();
	readFile();
	setupTransmit();
	doMath();
	writeFile();

	

def makeTime():
	global transmitTime
	global transmitDate
	global transmitRando
	global encodeDate
	global encodeTime
	global crazyMath
	global randDo
	randDo = random.randint(0,999)
	cleanTime = time.strftime('%H%M')
	cleanDate = time.strftime('%Y%m%d')
	transmitTime = int(cleanTime) + randDo
	transmitTime = int(transmitTime)**6
	transmitDate = int(cleanDate)**3
	transmitRando = int(randDo)**4
	crazyMath = cleanTime
	crazyMath += cleanDate



# I decided to use a random variable and add it to the time. The date will never repeat so there is
# no chance of a pattern being discovered by crackers. Hoewever, if a message was sent at the same 
# time everyday it would have the same time string. In order to confuse crackers we will also use
# a random number that we will transmit so that time is hidden
def setupTransmit():
	global transmitTime
	global transmitDate
	global encodedMessage
	transmitDateNew = str(transmitDate).zfill(30)
	transmitTimeNew = str(transmitTime).zfill(30)
	transmitRandoNew = str(transmitRando).zfill(30)
	encodedMessage += str(transmitDateNew)
	encodedMessage += str(transmitTimeNew)
	encodedMessage += str(transmitRandoNew)





def readFile():
	global workString
	openFile = sys.argv[1]
	workString = open(fileName, 'r').read()
	workString = workString.lower()
	if verbosity >= 1 :
		print (workString)

# this is the meat and potatos		
def doMath():
	global encodedMessage
	for char in workString:
			if char == "a":
				b = 12
			elif char == "b":
				b = 15
			elif char == "\n":
				b = 5
			elif char == "c":
				b = 17
			elif char == "d":
				b = 19
			elif char == "e":
				b = 23
			elif char == "f":
				b = 26
			elif char == "g":
				b = 28
			elif char == "h":
				b = 29
			elif char == "i":
				b = 37
			elif char == "j":
				b = 39
			elif char == "k":
				b = 40
			elif char == "l":
				b = 48
			elif char == "m":
				b = 51
			elif char == "n":
				b = 52
			elif char == "o":
				b = 53
			elif char == "p":
				b = 59
			elif char == "q":
				b = 70
			elif char == "r":
				b = 72
			elif char == "s":
				b = 77
			elif char == "t":
				b = 79
			elif char == "u":
				b = 80
			elif char == "v":
				b = 82
			elif char == "w":
				b = 86
			elif char == "x":
				b = 87
			elif char == "y":
				b = 90
			elif char == "z":
				b = 93
			elif char == " ":
				b = 99
			else:
				b = 0
			newLetter = int(b)*int(crazyMath)
			newLetter = newLetter**2
			newNewLetter = str(newLetter).zfill(30)
			encodedMessage += str(newNewLetter)
			

#Lets write this to an output file
def writeFile():
	if verbosity >= 1 :
		print(encodedMessage)
	if dryRun == 0 :
		f = open(outputFile, 'w')
		f.write(encodedMessage)
		f.close()

# Since EVERYTHING before this is definistions, running this one function, runs the program	
main();
