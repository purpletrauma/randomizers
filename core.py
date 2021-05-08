from theLists import *
from utilityFuncs import *
from random import sample, choice, choices

#The most basic randomizer. Take a runTime variable and return a list of results, pulled itself from a list.
def randomBall(runTimes):
	#I am astounded at how much easier this is this time.
	results = list()
	for i in range(runTimes):
		results.append(choice(randomLists.magicBallList))
	return results

def randomPhrase(runTimes):
	#Read an input file of text, make each line into a different list item.
	with open('input') as f:
		quoteFile = (f.readlines())
	#Remove the line breaks from the strings themselves.
	quoteFile = [word.strip() for word in quoteFile]
	#If the resulting list has fewer items than the number requested, then only return the quotes available.
	if len(quoteFile) < runTimes:
		runTimes = len(quoteFile)
	#Return the requested list of items, nonrepeating randomization.
	results = sample(quoteFile, runTimes)
	return results

#Revising my old code. Basically the same, just with better lists and data structure.
def randomLocation(runTimes, locationSize, isSilly):
	#First, since they can be altered, make the local variables equal the global ones.
	theLocation = randomLists.smallLocation.copy()
	theSociety = randomLists.smallSocialStructure.copy()
	theGenre = randomLists.genreList.copy()
	theAdjective = randomLists.adjectiveList.copy()
	theSpecies = randomLists.speciesList.copy()
	
	#As a standard, populate an empty list for variables that may need it.
	results = list()
	del results[:]
	finalAdjective = str()

	#Next, alter it as needed for the chosen size
	if locationSize == 1:
		theLocation +=randomLists.mediumLocation
		theSociety += randomLists.bigSocialStructure
	elif locationSize == 2:
		theLocation = randomLists.bigLocation
		theSociety = randomLists.bigSocialStructure
		
	#Silly mode alterations.
	if isSilly == True:
		theAdjective = theAdjective + randomLists.sillyAdjectiveList

	#Craft and return the results in a string.
	for i in range(runTimes):
		#Internal silly mode loop to deal with the silly adjectives.
		#As I tweaked how this worked, it became a more extensive population
		#of the variables before reaching the append command.
		if isSilly == True:
			finalLocation = choice(theAdjective) + " " + choice(theLocation)
			finalGenre = randomGenre(1) + " " + choice(theGenre)
			tempAdjective = sample(theAdjective,  2)
			for i in tempAdjective:
				finalAdjective += + i + " "
		else:
			finalLocation = choice(theLocation)
			finalGenre = choice(theGenre)
			finalAdjective = choice(theAdjective) + " "
		results.append("Genre: " + finalGenre + "\nLocation: " + finalLocation + "\nSocial Structure: " + choice(theSociety) + "\nSpecies: " + finalAdjective + choice(theSpecies) + " people\n")
		finalAdjective = ""
		finalLocation = ""
	return results

def randomGame(runTimes,  severity,  isSilly):
	results = list()
	del results[:]
	localAdjectives = randomLists.adjectiveList.copy()
	localPrompts = randomLists.promptsList.copy()
	localGenre = randomLists.genreList.copy()
	localMechanics = randomLists.generalMechanicsList.copy()
	localPersonality = randomLists.personalityList.copy()
	
	if isSilly == True:
		localAdjectives += randomLists.sillyAdjectiveList
		localMechanics += randomLists.specificMechanicsList
	
	for i in range(runTimes):
		buildResults = "Game prompt: A " + choice(localAdjectives) + " feeling " + choice(localPrompts)
		if severity > 0:
			buildResults += "\nSetting: A " + randomGenre(1) + " like " + choice(localGenre)
		if severity > 1:
			buildResults += "\nMechanics: With " + choice(localPersonality) + " style " + choice(localMechanics) + "\n"
		
		results.append(buildResults)

	return results

def randomGenre(runTimes):
	results = list()
	del results[:]
	
	if runTimes > 1:   
		for i in range(runTimes):
			results.append(choice(randomLists.punkGenre) + "punk")
	else:
		results = choice(randomLists.punkGenre) + "punk"
	
	return results

#Generating a random character.
def randomCharacter(runTimes, crossGenderPref, isKinky, bypassChecks, useSpecies, isSilly):
	results = list()
	localOutfit = randomLists.styleList.copy()
	if isSilly:
		localOutfit += randomLists.sillyStyleList.copy()
	del results[:]


	#Build the results together now that all the options have been squared away.
	for i in range(runTimes):
		theGender = choice(randomLists.genderList)
		finalAge = choices(randomLists.ageList, k=1,  weights=(1, 4, 4, 3, 3, 2, 1)) 
		buildResults = ""
		if useSpecies == 1:
			theSpecies = choice(randomLists.speciesList)
			buildResults = "Species: " + theSpecies + "\n"
		else:
			theSpecies = ""
		buildResults += "Age: " + choice(finalAge)  + "\n"
		buildResults += "Gender: " + theGender + "\n"
		buildResults += "Outfit Style: " + choice(localOutfit) + "\n"
		buildResults += "Outfit: " + outfitStyle(theSpecies, bypassChecks, theGender, crossGenderPref, isSilly) + "\n"
		buildResults += "Personality: " + choice(randomLists.personalityList)+ "\n"
		buildResults += "Primary and Secondary color: " + listToString(sample(randomLists.colorList,  2)) + "\n"
		buildResults += "Character quirk: "+ choice(randomLists.quirkList) + "\n"
		if isKinky == True:
			buildResults +="Kink: " + choice(randomLists.kinkList) + "\n"
		results.append(buildResults)
	return results

#Just a quick note.
# Weighted randomization: choices(theList, k=runTimes, weights=(#, #, #))
#The weights is for the list items in order.
#There needs to be a weight for each item.

