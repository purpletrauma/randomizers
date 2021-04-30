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

#This needed to be its own function: generating the gender randomization code. It needs to take one randomized variable, 3 user-chosen variables, and create a combination of 12 possible results based on those choices, one of which just alters the complexity of one of the others...
def outfitStyle(outfitDetail, theSpecies,  theGender, crossGenderPref,  isSilly):
    
    #A reminder, crossGenderPref is 0 standard, 1 for crossgender, 2 for anything goes.
    theOutfit = "nude"
    
    if crossGenderPref == 1:
        if theGender == "male":
            theGender = "female"
        else:
            theGender = "male"
    
    if outfitDetail == '1':
        localTop = randomLists.unisexTopList
        localBottom = randomLists.unisexBottomList
        localOuter = randomLists.unisexOuterList
        localAccessory = randomLists.unisexAccessoryList
        if isSilly:
            localTop = localTop + randomLists.sillyTopList
            localBottom = localBottom + randomLists.sillyBottomList
            localOuter = localOuter +randomLists.sillyOuterList
            localAccessory = localAccessory + randomLists.sillyAccessoryList

            
        if crossGenderPref == 2:
            localTop = localTop + randomLists.masculineTopList
            localBottom = localBottom + randomLists.masculineBottomList
            localOuter = localOuter + randomLists.masculineOuterList
            localAccessory = localAccessory + randomLists.masculineAccessoryList
            localTop = localTop + randomLists.feminineTopList
            localBottom = localBottom + randomLists.feminineBottomList
            localOuter = localOuter + randomLists.feminineOuterList
            localAccessory = localAccessory + randomLists.feminineAccessoryList
        elif theGender == "male":
            localTop = localTop + randomLists.masculineTopList
            localBottom = localBottom + randomLists.masculineBottomList
            localOuter = localOuter + randomLists.masculineOuterList
            localAccessory = localAccessory + randomLists.masculineAccessoryList
        else: 
            localTop = localTop + randomLists.feminineTopList
            localBottom = localBottom + randomLists.feminineBottomList
            localOuter = localOuter + randomLists.feminineOuterList
            localAccessory = localAccessory + randomLists.feminineAccessoryList
                
            
    else: 
        localOutfit = randomLists.unisexBodyList
        if isSilly:
            localOutfit = localOutfit + randomLists.sillyBodyList
        if crossGenderPref == 2:
            localOutfit = localOutfit + randomLists.feminineBodyList + randomLists.masculineBodyList
        elif theGender == "male":
           localOutfit = localOutfit + randomLists.masculineBodyList
        else: 
           localOutfit = localOutfit + randomLists.feminineBodyList

    #If only because it feels more coherent in the code, go ahead and find the results now.
    theTop = "\n    Top: " +  str(choice(localTop))
    theBottom = "\n     Bottom: " + str(choice(localBottom))
    theOuter =  "\n     Outerwear: " + str(choice(localOuter))
    theAccessory = "\n     Accessory: " + str(choice(localAccessory))    
    
    #True or false: does it have legs?
    hasLegs = leglessCheck(theSpecies)
    
    #Empty the bottom clothing if it came back false.
    if hasLegs == False:
        theBottom = ""
        
    if outfitDetail == '1':
        theOutfit = theTop + theBottom + theOuter + theAccessory
    else: 
        theOutfit = choice(localOutfit)
    return theOutfit
