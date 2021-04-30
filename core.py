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
    #Remove the "\n" from the list.
    quoteFile = [word.strip() for word in quoteFile]
    #If the resulting list has fewer items than the number requested, then reduce it to match.
    if len(quoteFile) < runTimes:
        runTimes = len(quoteFile)
    #Return the requested list of items.
    results = sample(quoteFile, runTimes)
    return results

#Revising my old code. Basically the same, just with better lists and data structure.
def randomLocation(runTimes, locationSize, isSilly):
    #First, since they can be altered, make the local variables equal the global ones.
    theLocation = randomLists.locationList
    theSociety = randomLists.societyList
    theGenre = randomLists.genreList
    theAdjective = randomLists.adjectiveList
    theSpecies = randomLists.speciesList
    results = list()
    del results[:]

    #Next, alter it as needed from input.
    if locationSize == 1:
        theLocation = randomLists.secondLocation + randomLists.locationList
        theSociety = randomLists.secondSociety + randomLists.societyList
    elif locationSize == 2:
        theLocation = randomLists.thirdLocation
        theSociety = randomLists.secondSociety
    if isSilly == True:
        newGenre = randomGenre(50)
        theGenre = newGenre
        theAdjective = randomLists.sillyAdjectiveList


    for i in range(runTimes):
        results.append("Genre: " + choice(theGenre) + "\nLocation: " + choice(theLocation) + "\nSocial Structure: " + choice(theSociety) + "\nSpecies: " + choice(theAdjective) + " " + choice(theSpecies) + ".\n")
    return results

def randomGame():
    return 

def randomGenre(runTimes):
    results = list()
    del results[:]
    
    for i in range(runTimes):
        results.append(choice(randomLists.punkGenre) + "punk")
    
    return results

#Had the idea, due to how simple it is, to make random genres as well.
def randomCharacter(runTimes, outfitDetail, crossGenderPref, isKinky,   isSilly):
    results = list()
    localOutfit = randomLists.styleList
    if isSilly:
        localOutfit = localOutfit + randomLists.sillyStyleList
    del results[:]


    for i in range(runTimes):
        theGender = choice(randomLists.genderList)
        finalAge = choices(randomLists.ageList, k=1,  weights=(1, 4, 4, 3, 3, 2, 1)) 
        theSpecies = choice(randomLists.singleSpeciesList)
        buildResults = "Species: " + theSpecies + "\n"
        buildResults += "Age: " + choice(finalAge)  + "\n"
        buildResults += "Gender: " + theGender + "\n"
        buildResults += "Outfit Style: " + choice(localOutfit) + "\n"
        buildResults += "Outfit: " + outfitStyle(outfitDetail, theSpecies,  theGender, crossGenderPref, isSilly) + "\n"
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

