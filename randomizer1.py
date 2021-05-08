from core import *


def run8Ball(runTimes):
	 getResults = randomBall(runTimes)
	 
	 return getResults

def runPhrases(runTimes):
	getResults = randomPhrase(runTimes)
	
	return getResults

def runLocation(runTimes):
	locationSize = int(input("From 0 to 2, how big is the location?\n"))
	if locationSize not in range(3):
		print("I don't know what to tell ya, man.")
		quit()
	isSilly = sillyCheck()

	getResults = randomLocation(runTimes, locationSize, isSilly)
	
	return getResults

def runGenre(runTimes):
	getResults = randomGenre(runTimes)
	
	return getResults

def runCharacter(runTimes):
	
	#Check if user wants a kink.
	getKink = int(input("Do you want a kink? 0 no 1 yes\n"))
	
	if getKink == 1:
		isKinky = True
	else:
		isKinky = False
		
	#Check if other checks can be skipped.
	bypassChecks = int(input("Anything goes outfit? (Will bypass all checks for appropriateness) 0 no 1 yes\n"))
	
	if bypassChecks == 1:
		crossGenderPref = 0
		isSilly = True
	else:
		crossGenderPref = int(input("Crossdressing? 0 no 1 yes 2 anything\n"))
		isSilly = sillyCheck()

	#Bypass for the species randomization.
	useSpecies = int(input("Do you want a random species? 0 no 1 yes\n"))
	
	getResults = randomCharacter(runTimes, crossGenderPref, isKinky, bypassChecks, useSpecies, isSilly)    
	return getResults

def runGame(runTimes):
	isSilly = sillyCheck()
	getSeverity = int(input("Do you want light, medium, or heavy results? 0 to 2.\n"))
	
	getResults = randomGame(runTimes,  getSeverity,  isSilly)
	return getResults

def sillyCheck():
	getSilly = int(input("Run in silly mode? 0 no 1 yes.\n"))
	if getSilly == 1:
		isSilly = True
	else:
		isSilly = False
	return isSilly

while True:
	
	print('Pick your randomizer!\n')
	whichOne = int(input("Enter 0 for 8ball, 1 for phrases, 2 for location, 3 for genre, 4 for characters, 5 for game prompt.\n"))
	runTimes = int(input("How many times do you want to run this?\n"))
	theResults = list()

	if whichOne == 0:
		theResults = run8Ball(runTimes)
	elif whichOne == 1:
	   theResults = runPhrases(runTimes)
	elif whichOne == 2:
		theResults = runLocation(runTimes)
	elif whichOne == 3:
		theResults = runGenre(runTimes)
	elif whichOne == 4:
	   theResults = runCharacter(runTimes)
	elif whichOne == 5:
		theResults = runGame(runTimes)
	else:
		print('I dunno what to tell ya, man.')
		quit()

	for i in theResults:
		print(i)
	goAgain = input('\nDo you want to go again? y/n\n')
	if goAgain != 'y':
		quit()

