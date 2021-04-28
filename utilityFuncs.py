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
def leglessCheck(species):
    hasLegs = True
    leglessList = randomLists.leglessSpeciesList
    for i in leglessList:
        if i == species:
            hasLegs = False
    return hasLegs

#This needed to be its own function: generating the gender randomization code. It needs to take one randomized variable, 3 user-chosen variables, and create a combination of 12 possible results based on those choices, one of which just alters the complexity of one of the others...
def outfitStyle(outfitDetail,  theGender, crossGenderPref,  isSilly):
    
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
            localAccessory = localAccessry + randomLists.masculineAccessoryList
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
        theOutfit = "undetailed "
        if isSilly:
            theOutfit +="silly "
            
        if crossGenderPref == 2:
            theOutfit += "genderneutral"
        elif theGender == "male":
            theOutfit += "mascule"
        else: 
            theOutfit += "feminine"

    
    if outfitDetail == '1':
        theOutfit = "\n     Top: " + str(choice(localTop)) + "\n     Bottom: " + str(choice(localBottom)) + "\n     Outerwear: " + str(choice(localOuter)) + "\n     Accessory: " + str(choice(localAccessory))
    else: 
        theOutfit = choice(localOutfit)
    return theOutfit
