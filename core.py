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
		#I just shoved this in real quick to use the new list.
		tempSpecies = randomLists.speciesList + randomLists.speciesAdjectiveList
		if useSpecies == 1:
			theSpecies = choice(tempSpecies)
			buildResults = "Species: " + theSpecies + "\n"
		else:
			theSpecies = ""
			
		buildLikes = sample(randomLists.likesList, 4)
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
		buildResults += "Outfit: " + buildOutfit(theSpecies, bypassChecks, theGender, crossGenderPref, isSilly) + "\n"
		buildResults += "Personality: " + choice(randomLists.personalityList)+ "\n"
		buildResults += "Likes: " + theLikes + "\n"
		buildResults += "Dislikes: " + theDislikes + "\n"
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



#This needed to be its own function: generating the gender randomization code. 
#It needs to take one randomized variable, 3 user-chosen variables, and create a combination 
#of 12 possible results based on those choices, one of which just alters the complexity of one of the others...
def buildOutfit(theSpecies, bypassChecks, theGender, crossGenderPref, isSilly):
	
	#A reminder, crossGenderPref is 0 standard, 1 for crossdresser, 2 for anything goes.	
	
	
	#Default unisex items added to lists.
	#Also, since I need the external lists to remain unchanging, .copy() them instead of =.
	localTop = randomLists.unisexTopList.copy()
	localBottom = randomLists.unisexBottomList.copy()
	localOuter = randomLists.unisexOuterList.copy()
	localShoes = randomLists.unisexShoesList.copy()
	localHeld = randomLists.unisexHeldAccessories.copy()
	localHead = randomLists.unisexHeadAccessories.copy()
	localWaist = randomLists.unisexWaistAccessories.copy()
	localFace = randomLists.unisexFaceAccessories.copy()
	localNeck = randomLists.unisexNeckAccessories.copy()
	localHand = randomLists.unisexHandAccessories.copy()
	
	
	#Get the silly check out of the way.
	if isSilly:
		localTop += randomLists.sillyTopList
		localBottom += randomLists.sillyBottomList
		localOuter += randomLists.sillyOuterList
		localShoes += randomLists.sillyShoesList
		localHeld += randomLists.sillyHeldAccessories
		localHead += randomLists.sillyHeadAccessories
		localWaist += randomLists.sillyWaistAccessories
		localFace += randomLists.sillyFaceAccessories
		localNeck += randomLists.sillyNeckAccessories
		localHand += randomLists.sillyHandAccessories	
	
	#If you bypass checks, just add everything.
	if bypassChecks:
		localTop += randomLists.masculineTopList + randomLists.feminineTopList
		localBottom += randomLists.masculineBottomList + randomLists.feminineBottomList
		localOuter += randomLists.masculineOuterList + randomLists.feminineOuterList
		localShoes += randomLists.feminineShoesList + randomLists.masculineShoesList + randomLists.winterShoesList + randomLists.summerShoesList
		localHeld += randomLists.feminineHeldAccessories + randomLists.masculineHeldAccessories
		localHead += randomLists.feminineHeadAccessories + randomLists.masculineHeadAccessories
		localWaist += randomLists.feminineWaistAccessories + randomLists.masculineWaistAccessories
		localFace += randomLists.feminineFaceAccessories + randomLists.masculineFaceAccessories
		localNeck += randomLists.feminineNeckAccessories + randomLists.masculineNeckAccessories
		localHand += randomLists.feminineHandAccessories + randomLists.masculineHandAccessories
		
		#Choose options.
		finalTop = choice(localTop)
		finalBottom = choice(localBottom)
		finalOuter = choice(localOuter)
		finalShoes = choice(localShoes)
		finalHeld = choice(localHeld)
		finalHead = choice(localHead)
		finalWaist = choice(localWaist)
		finalFace = choice(localFace)
		finalNeck = choice(localNeck)
		finalHand = choice(localHand)
	#All other checks in the "else" category.
	else:
		#If crossgender, swap gender from selected one.
		if crossGenderPref == 1:
			if theGender == "male":
				theGender = "female"
			else:
				theGender = "male"
		
		#Add everything if anything goes gender-wise.
		if crossGenderPref == 2:
			localTop += randomLists.feminineTopList + randomLists.feminineTopList
			localBottom += randomLists.feminineBottomList + randomLists.masculineBottomList
			localOuter += randomLists.feminineOuterList + randomLists.masculineOuterList
			localShoes += randomLists.feminineShoesList
			localHeld += randomLists.feminineHeldAccessories + randomLists.masculineHeldAccessories
			localHead += randomLists.feminineHeadAccessories + randomLists.masculineHeadAccessories
			localWaist += randomLists.feminineWaistAccessories + randomLists.masculineWaistAccessories
			localFace += randomLists.feminineFaceAccessories + randomLists.masculineFaceAccessories
			localNeck += randomLists.feminineNeckAccessories + randomLists.masculineNeckAccessories
			localHand += randomLists.feminineHandAccessories + randomLists.masculineHandAccessories
		# Add masculine items if male.
		elif theGender == "male":
			localTop += randomLists.masculineTopList
			localBottom += randomLists.masculineBottomList
			localOuter += randomLists.masculineOuterList
			localShoes += randomLists.masculineShoesList
			localHeld += randomLists.masculineHeldAccessories
			localHead += randomLists.masculineHeadAccessories
			localWaist += randomLists.masculineWaistAccessories
			localFace += randomLists.masculineFaceAccessories
			localNeck += randomLists.masculineNeckAccessories
			localHand += randomLists.masculineHandAccessories
		#Add feminine items if female.
		else: 
			localTop += randomLists.feminineTopList
			localBottom += randomLists.feminineBottomList
			localOuter += randomLists.feminineOuterList
			localShoes += randomLists.feminineShoesList
			localHeld += randomLists.feminineHeldAccessories
			localHead += randomLists.feminineHeadAccessories
			localWaist += randomLists.feminineWaistAccessories
			localFace += randomLists.feminineFaceAccessories
			localNeck += randomLists.feminineNeckAccessories
			localHand += randomLists.feminineHandAccessories
			#Bonnets!
			if isSilly:
				localHead += randomLists.feminineSillyHeadList
			
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
		if checkVariable(randomLists.collaredShirtList, finalTop):
			localNeck += randomLists.tieList
			finalNeck = choice(localNeck)
		theAccessories = [finalHeld, finalHead, finalWaist, finalFace, finalNeck, finalHand]
		finalAccessories = sample(theAccessories, 2)
		#Such a minor check, but I wanted suspenders if appropriate..
		if not checkVariable(randomLists.leglessSpeciesList, theSpecies):
			localWaist.append("suspenders")
			finalWaist = choice(localWaist)
		
		
		#Check for winter/summer coat, 
		weatherWear = checkVariable(randomLists.winterOuterwearList, finalOuter)
		if checkVariable(randomLists.winterOuterwearList, finalOuter):
			localShoes += randomLists.winterShoesList
			finalShoes = choice(localShoes)
			localHead += randomLists.winterHeadAccessories
			finalHead = choice(localHead)
		elif checkVariable(randomLists.summerOuterwearList, finalOuter):
			localShoes += randomLists.summerShoesList
			finalShoes = choice(localShoes)
			localHead += randomLists.summerHeadAccessories
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
	if checkVariable(randomLists.leglessSpeciesList, theSpecies):
		theBottom = ""
		theShoes = ""
		
	theOutfit = theTop + theBottom + theOuter + theShoes + theAccessories
	

	return theOutfit
