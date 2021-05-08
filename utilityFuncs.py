from theLists import *
from random import choice

#Code pulled from example because once finding there wasn't an existing function, I didn't want to bother.
def listToString(s): 
	
	# initialize an empty string
	str1 = "" 
	
	# traverse in the string  
	for ele in s: 
		str1 += " " + ele  
	
	# return string  
	return str1 

#Checking for whether a species has legs to wear pants with.
#This might not be the best results, but I kept reworking it until I realized the check for the results of this function was looking for a string "False" instead of a boolean False.
def leglessCheck(species):
	hasLegs = True
	leglessList = randomLists.leglessSpeciesList
	for i in leglessList:
		if i in str(species):
			hasLegs = False
	return hasLegs


def weatherCheck(outerwear):
	weatherAppropriate = 0
	winterList = randomLists.winterOuterwearList
	summerList = randomLists.warmOuterwearList
	for i in winterList:
		if i in str(outerwear):
			weatherAppropriate = 1
	for i in summerList:
		if i in str(outerwear):
			weatherAppropriate = 2
			
	return weatherAppropriate
	


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
	
	#Get the silly check out of the way.
	if isSilly:
		localTop += randomLists.sillyTopList
		localBottom += randomLists.sillyBottomList
		localOuter += randomLists.sillyOuterList
		localShoes += randomLists.sillyShoesList		
	
	#If you bypass checks, just add everything.
	if bypassChecks == 1:
		localTop += randomLists.masculineTopList + randomLists.feminineTopList
		localBottom += randomLists.masculineBottomList + randomLists.feminineBottomList
		localOuter += randomLists.masculineOuterList + randomLists.feminineOuterList
		localShoes += randomLists.feminineShoesList + randomLists.winterShoesList + randomLists.warmShoesList
		
		#Choose options.
		finalTop = choice(localTop)
		finalBottom = choice(localBottom)
		finalOuter = choice(localOuter)
		finalShoes = choice(localShoes)
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
		# Add masculine items if male.
		elif theGender == "male":
			localTop += randomLists.masculineTopList
			localBottom += randomLists.masculineBottomList
			localOuter += randomLists.masculineOuterList
		#Add feminine items if female.
		else: 
			localTop += randomLists.feminineTopList
			localBottom += randomLists.feminineBottomList
			localOuter += randomLists.feminineOuterList
			localShoes += randomLists.feminineShoesList
			
		#Populate the lists.
		finalTop = choice(localTop)
		finalBottom = choice(localBottom)
		finalOuter = choice(localOuter)
		finalShoes = choice(localShoes)

		
		#Check for winter/summer coat, 
		weatherWear = weatherCheck(finalOuter)
		if weatherWear == 1:
			localShoes += randomLists.winterShoesList
			finalShoes = choice(localShoes)
		elif weatherWear == 2:
			localShoes += randomLists.warmShoesList
			finalShoes = choice(localShoes)

			


			
			
			
	
	#If only because it feels more coherent in the code, go ahead and find the results now.
	theTop = "\n     Top: " +  finalTop
	theBottom = "\n     Bottom: " + finalBottom
	theOuter =  "\n     Outerwear: " + finalOuter
	theShoes = "\n     Shoes: " + finalShoes
	
	#True or false: does it have legs?
	hasLegs = leglessCheck(theSpecies)
	
	#Empty the bottom clothing if it came back false.
	if hasLegs == False:
		theBottom = ""
		theShoes = ""
		
	theOutfit = theTop + theBottom + theOuter + theShoes
	

	return theOutfit
