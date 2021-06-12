#!/usr/bin/env python3

"""
This file is for the designated randomizers.

They take the input and returns a list.
"""

from theLists import *
from utilityFuncs import *
from random import sample, choice, choices

#The most basic randomizer. Take a runTime variable and return a list of results, pulled itself from a list.
def randomBall(runTimes):
	#I am astounded at how much easier this is this time.
	results = list()
	for i in range(runTimes):
		results.append(choice(magicBall.getList()))
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
	theLocation = locationLists.small()
	theSociety = socialLists.small()
	theGenre = genres.getList()
	theAdjective = adjectives.getList()
	theSpecies = species.getList()
	
	#As a standard, populate an empty list for variables that may need it.
	results = list()
	del results[:]
	finalAdjective = str()

	#Next, alter it as needed for the chosen size
	if locationSize == 1:
		theLocation +=locationLists.medium()
		theSociety += socialLists.large()
	elif locationSize == 2:
		theLocation = locationLists.large()
		theSociety = socialLists.large()
		
	#Silly mode alterations.
	if isSilly == True:
		theAdjective += adjectives.getSilly()

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
				finalAdjective += i + " "
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
	localAdjectives = adjectives.getList()
	localPrompts = prompts.getList()
	localGenre = genres.getList()
	localMechanics = mechGen.getList()
	localPersonality = personalities.getList()
	
	if isSilly == True:
		localAdjectives += adjectives.getSilly()
		localMechanics += mechSpef.getList()
	
	for i in range(runTimes):
		buildResults = "Game prompt: A " + choice(localAdjectives) + " feeling " + choice(localPrompts)
		if severity > 0:
			buildResults += "\nSetting: A " + randomGenre(1) + " like" + choice(localGenre)
		if severity > 1:
			buildResults += "\nMechanics: With " + choice(localPersonality) + " style " + choice(localMechanics) + "\n"
		
		results.append(buildResults)

	return results

def randomGenre(runTimes):
	results = list()
	del results[:]
	
	if runTimes > 1:   
		for i in range(runTimes):
			results.append(choice(punks.getList()) + "punk")
	else:
		results = choice(punks.getList()) + "punk"
	
	return results

#Generating a random character.
def randomCharacter(runTimes, crossGenderPref, isKinky, bypassChecks, useSpecies, isSilly):
	results = []
	localOutfit = styleLists.getList()
	if isSilly:
		localOutfit += styleLists.getSilly()
	del results[:]


	#Build the results together now that all the options have been squared away.
	for i in range(runTimes):
		theGender = choice(genderList)
		finalAge = choices(ages.getList(), k=1,  weights=(1, 4, 4, 3, 3, 2, 1)) 
		buildResults = ""
		if useSpecies == 1 and isSilly:
			theSpecies = choice(species.getSilly()) + " " + choice(species.getList())
			buildResults = "Species: " + theSpecies + "\n"	
		elif useSpecies == 1:
			theSpecies = choice(species.everything())
			buildResults = "Species: " + theSpecies + "\n"
		else:
			theSpecies = ""
			
		buildLikes = sample(likes.getList(), 4)
		theLikes = ""
		theDislikes = ""

		#Use enumeration to alternate likes and dislikes for the length of the list.
		for n, i in enumerate(buildLikes):
			if n % 2 == 0:
				theLikes += i + ", "
			else:
				theDislikes += i + ", "
		theLikes = theLikes[:len(theLikes)-2]
		theDislikes = theDislikes[:len(theDislikes)-2]
		
		buildResults += "Age: " + choice(finalAge)  + "\n"
		buildResults += "Gender: " + theGender + "\n"
		buildResults += "Outfit Style: " + choice(localOutfit) + "\n"
		buildResults += "Outfit: " + outfitStyle(theSpecies, bypassChecks, theGender, crossGenderPref, isSilly) + "\n"
		buildResults += "Personality: " + choice(personalities.getList())+ "\n"
		buildResults += "Likes: " + theLikes + "\n"
		buildResults += "Dislikes: " + theDislikes + "\n"
		buildResults += "Primary and Secondary color: " + listToString(sample(colors.getList(),  2)) + "\n"
		buildResults += "Character quirk: "+ choice(quirks.getList()) + "\n"
		if isKinky == True:
			buildResults +="Kink: " + choice(kinks.getList()) + "\n"
		results.append(buildResults)
	return results

#Just a quick note.
# Weighted randomization: choices(theList, k=runTimes, weights=(#, #, #))
#The weights is for the list items in order.
#There needs to be a weight for each item.



def outfitStyle(theSpecies, bypassChecks, theGender, crossGenderPref, isSilly):
	
	#A reminder, crossGenderPref is 0 standard, 1 for crossdresser, 2 for anything goes.	
	
	

	
	#If you bypass checks, just add everything.
	if bypassChecks == 1:
		localTop = topLists.everything()
		localBottom = bottomLists.everything()
		localOuter = outerLists.everything()
		localShoes = shoeLists.everything()
		localHeld = heldLists.everything()
		localHead = headLists.everything()
		localWaist = waistLists.everything()
		localFace = faceLists.everything()
		localNeck = neckLists.everything()
		localHand = handLists.everything()
	else:
		#Default unisex items added to lists.
		localTop = []
		localBottom = []
		localOuter = []
		localShoes = []
		localHeld = []
		localHead = []
		localWaist = []
		localFace = []
		localNeck = []
		localHand = []
		
		
		#Get the silly check out of the way.
		if isSilly:
			localTop += topLists.silly()
			localBottom += bottomLists.silly()
			localOuter += outerLists.silly()
			localShoes += shoeLists.silly()
			localHeld += heldLists.silly()
			localHead += headLists.silly()
			localWaist += waistLists.silly()
			localFace += faceLists.silly()
			localNeck += neckLists.silly()
			localHand += handLists.silly()
		#If crossgender, swap gender from selected one.
		if crossGenderPref == 1:
			if theGender == "male":
				theGender = "female"
			else:
				theGender = "male"
		
		#Add everything if anything goes gender-wise.
		if crossGenderPref == 2:
			localTop += topLists.cross()
			localBottom += bottomLists.cross()
			localOuter += outerLists.cross()
			localShoes += shoeLists.cross()
			localHeld += heldLists.cross()
			localHead += headLists.cross()
			localWaist += waistLists.cross()
			localFace += faceLists.cross()
			localNeck += neckLists.cross()
			localHand += handLists.cross()
		# Add masculine items if male.
		elif theGender == "male":
			localTop += topLists.masculine()
			localBottom += bottomLists.masculine()
			localOuter += outerLists.masculine()
			localShoes += shoeLists.masculine()
			localHeld += heldLists.masculine()
			localHead += headLists.masculine()
			localWaist += waistLists.masculine()
			localFace += faceLists.masculine()
			localNeck += neckLists.masculine()
			localHand += handLists.masculine()
		#After those checks, can assume feminine outfit.
		else: 
			localTop += topLists.feminine()
			localBottom += bottomLists.feminine()
			localOuter += outerLists.feminine()
			localShoes += shoeLists.feminine()
			localHeld += heldLists.feminine()
			localHead += headLists.feminine()
			localWaist += waistLists.feminine()
			localFace += faceLists.feminine()
			localNeck += neckLists.feminine()
			localHand += handLists.feminine()
			#Bonnets!
			if isSilly:
				localHead += femSilHead.getList()
		
	#Populate the lists.
	finalTop = choice(localTop)
	finalBottom = choice(localBottom)
	finalOuter = choice(localOuter)
	finalShoes = choice(localShoes)
	#Accessories are a little different.
	finalHeld = choice(localHeld)
	finalHead = choice(localHead)
	finalWaist = choice(localWaist)
	finalFace = choice(localFace)
	finalNeck = choice(localNeck)
	finalHand = choice(localHand)
	#Check for a collared shirt.
	if checkVariable(collarTest.getList(), finalTop):
		localNeck += tieList.getList()
		if isSilly:
			localNeck +=tieList.getSilly()
		finalNeck = choice(localNeck)
	theAccessories = [finalHeld, finalHead, finalWaist, finalFace, finalNeck, finalHand]
	finalAccessories = sample(theAccessories, 2)
	#Such a minor check, but I wanted suspenders if appropriate..
	if not checkVariable(leglessTest.getList(), theSpecies):
		localWaist.append("suspenders")
		finalWaist = choice(localWaist)
	
	#Need to skip if bypass added everything.
	#Don't like adding to the list outside of the ifelse loop, but not sure how to do this one.
	if not bypassChecks == 1:
	#Check for winter/summer coat, 
		if checkVariable(outerLists.winter(), finalOuter):
			localShoes += shoeLists.winter()
			finalShoes = choice(localShoes)
			localHead += headLists.winter()
			finalHead = choice(localHead)
		elif checkVariable(outerLists.summer(), finalOuter):
			localShoes += shoeLists.summer()
			finalShoes = choice(localShoes)
			localHead += headLists.summer()
			finalHead = choice(localHead)
	


			
			
			
	
	#If only because it feels more coherent in the code, go ahead and find the results now.
	theTop = "\n     Top: " +  finalTop
	theBottom = "\n     Bottom: " + finalBottom
	theOuter =  "\n     Outerwear: " + finalOuter
	theShoes = "\n     Shoes: " + finalShoes
	theAccessories = "\n     Accessories:"
	for i in finalAccessories:
		theAccessories += " " + i + ","
	#Remove the extra comma at the end.
	theAccessories = theAccessories[:len(theAccessories)-1]
	#Empty the bottom clothing if the species matches with legless species.
	if checkVariable(leglessTest.getList(), theSpecies):
		theBottom = ""
		theShoes = ""
		
	theOutfit = theTop + theBottom + theOuter + theShoes + theAccessories
	

	return theOutfit
