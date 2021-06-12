#!/usr/bin/env python3

"""
A file for smaller misc definitions that have more general use throughout the different scripts.

"""

from theLists import *
from random import choice, sample

#Code pulled from example because once finding there wasn't an existing function, I didn't want to bother.
def listToString(s): 
	
	# initialize an empty string
	str1 = "" 
	
	# traverse in the string  
	for ele in s: 
		str1 += ele + " "
	#My addition: spaces in between, remove the extra at the end.
	str1 = str1[:len(str1)-1]
	# return string  
	return str1 

#Replaced 3 functions with this one: nice.	
def checkVariable(testList, testVariable):
	results = False
	for i in testList:
		if i in str(testVariable):
			results = True
	return results

def isItTrue(testVariable):
	isTrue = False
	if int(testVariable) == 1:
		isTrue = True
	return isTrue
	
def sillyCheck():
	getSilly = input("Run in silly mode? 0 no 1 yes.\n")
	isSilly = isItTrue(getSilly)
	return isSilly
