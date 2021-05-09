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

#This needed to be its own function: generating the gender randomization code. 
#It needs to take one randomized variable, 3 user-chosen variables, and create a combination 
#of 12 possible results based on those choices, one of which just alters the complexity of one of the others...
def outfitStyle(theSpecies, bypassChecks, theGender, crossGenderPref, isSilly):
	
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
	if bypassChecks == 1:
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
