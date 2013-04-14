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
import os # we might not need this
import sys # we might not need this
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

	readMessage();
	receiveSalt();
	doMoreMath();
	writeDecodedFile();


def readMessage():
	global workStringTwo
	openFile = sys.argv[1]
	workStringTwo = open(fileName, 'r').read()
	if verbosity >= 1 :
		print (workStringTwo)


def receiveSalt():
	global receivedTime
	global receivedDate
	global receivedRando
	global decodedMessage
	global workStringTwo
	global crazyMathTwo
	decodedMessage = ""
	receivedDate = workStringTwo[:30]
	receivedDate = float(receivedDate)
	workStringTwo = workStringTwo[30:]
	receivedTime = workStringTwo[:30]
	receivedTime = float(receivedTime)
	workStringTwo = workStringTwo[30:]
	receivedRando = workStringTwo[:30]
	receivedRando = float(receivedRando)
	workStringTwo = workStringTwo[30:]
	realRando = math.pow(receivedRando, 1/4)
	realRando = float(realRando)
	realTime = math.pow(receivedTime, 1/6)
	realTime = realTime - realRando
	realTime = int(realTime)
	realDate = math.pow(receivedDate, 1/3)
	realDate = int(realDate)
	decodedMessage += "Time was:"
	decodedMessage += str(realTime)
	decodedMessage += "\n"	
	decodedMessage += "Date was:"
	decodedMessage += str(realDate)
	decodedMessage += "\n"	
	decodedMessage += "\n"
	realTime = str(realTime)
	realDate = str(realDate)
	crazyMathTwo = realTime
	crazyMathTwo += realDate
	crazyMathTwo = int(crazyMathTwo)


# this is the meat and potatos		
def doMoreMath():
	global workStringTwo
	global testVal
	global decodedMessage
	testVal = 0
	while len(workStringTwo) > 1:
		workStringThree = workStringTwo[:30]
		workStringThree = float(workStringThree)
		testVal = math.pow(workStringThree, 1/2)
		testVal = testVal / int(crazyMathTwo)
		testVal = int(testVal)
		if testVal == 12:
			b = "a"
		elif testVal == 15:
			b = "b"
		elif testVal == 5:
			b = "\n"
		elif testVal == 17:
			b = "c"
		elif testVal == 19:
			b = "d"
		elif testVal == 23:
			b = "e"
		elif testVal == 26:
			b = "f"
		elif testVal == 28:
			b = "g"
		elif testVal == 29:
			b = "h"
		elif testVal == 37:
			b = "i"
		elif testVal == 39:
			b = "j"
		elif testVal == 40:
			b = "k"
		elif testVal == 48:
			b = "l"
		elif testVal == 51:
			b = "m"
		elif testVal == 52:
			b = "n"
		elif testVal == 53:
			b = "o"
		elif testVal == 59:
			b = "p"
		elif testVal == 70:
			b = "q"
		elif testVal == 72:
			b = "r"
		elif testVal == 77:
			b = "s"
		elif testVal == 79:
			b = "t"
		elif testVal == 80:
			b = "u"
		elif testVal == 82:
			b = "v"
		elif testVal == 86:
			b = "w"
		elif testVal == 87:
			b = "x"
		elif testVal == 90:
			b = "y"
		elif testVal == 93:
			b = "z"
		elif testVal == 99:
			b = " "
		else:
			b = ""
		newLetter = str(b)
		decodedMessage += str(newLetter)
		workStringTwo = workStringTwo[30:]
			

#Lets write this to an output file
def writeDecodedFile():
	if verbosity >= 1 :
		print(decodedMessage)
	if dryRun == 0 :
		f = open(outputFile, 'w')
		f.write(decodedMessage)
		f.close()

# Since EVERYTHING before this is definistions, running this one function, runs the program	
main();

