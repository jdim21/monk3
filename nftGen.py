import os, sys
import random
from PIL import Image
from draw.drawType import drawSolanaBackground, drawType
from draw.drawBody import drawBody
from draw.drawNeck import drawNeck
from draw.drawHat import drawHat
from draw.drawEyes import drawEyes
from draw.drawMouth import drawMouth
from traitCount import traitCountDict
from traitEncodings import TRAIT_ENCODINGS

numTraits = 6
traitAtIndex = ["type", "body", "neck", "mouth", "hat", "eyes"]
hatsToDrawSecond = ["f", "W"]
mouthsToDrawLast = ["g", "i", "a"]
typesOfCaps = ["N", "O", "P", "Q", "R", "S"]

def main():
    traitsDict = buildTraitsDict()
    random.seed(533351)

    makeNewImage(5001, "t_____")
    # makeNewImage(5001, "ni_hr_")
    # makeNewImage(5002, "i_____")
    # makeNewImage(5003, "z_____")
    # makeNewImage(5004, "a_____")
    # makeNewImage(5005, "v_____")
    # makeNewImage(5006, "s_____")
    # makeNewImage(5007, "n_____")
    # makeNewImage(5008, "l_____")
    # makeNewImage(5009, "d_____")
    # makeNewImage(5010, "b_____")
    # makeNewImage(5011, "r_____")
    # makeNewImage(5012, "k_____")

    dogeId = 1
    dupesRetry = 0
    timeoutsTotal = 0
    allRolls = []
    while len(traitsDict["type"]) > 0:
        foundRollOrTimeout = False
        while not foundRollOrTimeout:
            roll = makeTraitsRoll(traitsDict)
            if roll not in allRolls:
                allRolls.append(roll)
                foundRollOrTimeout = True
                makeNewImage(dogeId, roll)
                dogeId = dogeId + 1
            else:
                traitsDict[traitAtIndex[0]].append(roll[0])
                traitsDict[traitAtIndex[1]].append(roll[1])
                traitsDict[traitAtIndex[2]].append(roll[2])
                traitsDict[traitAtIndex[3]].append(roll[3])
                traitsDict[traitAtIndex[4]].append(roll[4])
                traitsDict[traitAtIndex[5]].append(roll[5])
            if dupesRetry >= 100:
                print("Timed out trying to de-dupe: " + roll)
                foundRollOrTimeout = True
                timeoutsTotal = timeoutsTotal + 1
                if timeoutsTotal >= 100:
                    print("Too many timeouts. Exiting.")
                    exit(-1)
            dupesRetry = dupesRetry + 1
        dupesRetry = 0

def makeNewImage(iter, traits):

    # Draw the tiny version
    im = Image.new('RGBA', (24, 24))
    drawSolanaBackground(im)
    drawType(im, traits[0])
    #drawNeck(im, traits[2])
    drawBody(im, traits[1], traits[0])
    if (traits[3] not in mouthsToDrawLast):
        drawMouth(im, traits[3], traits[0])
    if (traits[4] in hatsToDrawSecond):
        drawEyes(im, traits[5], traits[0])
        drawHat(im, traits[4], traits[0])
    else:
        drawHat(im, traits[4], traits[0])
        drawEyes(im, traits[5], traits[0])
    if (traits[3] in mouthsToDrawLast):
        drawMouth(im, traits[3], traits[0])
    #smallFileName = "images/" + str(iter) + "." + l1 + l2 + l3 + ".png"
    #im.save(smallFileName, "PNG")
    
    # Make a larger version which looks nicer
    im2 = im.resize((240, 240), resample=Image.NEAREST)
    #im2.show()
    largeFileName = "images\\" + str(iter) + "." + traits + ".240.png"
    im2.save(largeFileName, "PNG")

def buildTraitsDict():
    traitsDict = { "type": [], "body": [], "neck": [], "mouth": [], "hat": [], "eyes": [] }

    useManualDict = False
    if useManualDict:
        traitsDict = {
            "type": ["n", "l", "d", "b", "r", "k", "n", "v", "z", "a", "n", "n", "n", "n", "n", "n", "n"], 
            "body": ["p", "w", "l", "c", "i", "k", "o", "s", "n", "y", "r", "d", "t", "_", "_", "_", "_"], 
            "neck": ["b", "r", "g", "c", "y", "o", "e", "s", "u", "d", "f", "n", "p", "_", "_", "_", "_"], 
            "mouth": ["b", "t", "j", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"], 
            "hat": ["p", "b", "r", "g", "w", "m", "z", "c", "f", "j", "k", "o", "n", "l", "h", "_", "_"],
            "eyes": ["p", "c", "a", "h", "y", "g", "s", "t", "n", "n", "v", "_", "_", "_", "_", "_", "_"]
        }
    else:
        for key in TRAIT_ENCODINGS.keys():
            #print("key: " + str(key))
            for traitEncoding in TRAIT_ENCODINGS[key]:
                currTrait = TRAIT_ENCODINGS[key][traitEncoding]
                #print("trait: " + currTrait)
                if currTrait in traitCountDict[key]:
                    for i in range(traitCountDict[key][currTrait]):
                        traitsDict[key].append(traitEncoding)

    for key in traitsDict.keys():
        while len(traitsDict[key]) < len(traitsDict["type"]):
            traitsDict[key].append("_")

    #print("builtDict: " + str(traitsDict))

    # Check that all entries are equal, else fail
    expectedLen = len(traitsDict["type"])
    for key in traitsDict.keys():
        if len(traitsDict[key]) != expectedLen:
            print("Error in buildTraitsDict(). " + str(key) + " does not match expectedLen: " + str(expectedLen) + " (" + str(len(traitsDict[key])) +")")
            exit(-1)

    return traitsDict

def makeTraitsRoll(traitsDict):
    traitStr = ""
    traitList = ["type", "body", "neck", "mouth", "hat", "eyes"]
    for trait in traitList:
        roll = random.choice(traitsDict[trait])
        traitsDict[trait].remove(roll)
        traitStr = traitStr + roll
    # Hack to undo 9 out of 10 full trait rolls
    if not "_" in traitStr:
        ninetyEightPercentChance = random.randrange(100)
        if ninetyEightPercentChance >= 98:
            # Remove two traits
            slots = [1, 2, 3, 4, 5]
            undoSlot1 = random.choice(slots)
            slots.remove(undoSlot1)
            traitsDict[traitList[undoSlot1]].append(traitStr[undoSlot1])
            traitStr = traitStr[0:undoSlot1] + "_" + traitStr[undoSlot1+1:numTraits]
            undoSlot2 = random.choice(slots)
            slots.remove(undoSlot2)
            traitsDict[traitList[undoSlot2]].append(traitStr[undoSlot2])
            traitStr = traitStr[0:undoSlot2] + "_" + traitStr[undoSlot2+1:numTraits]

    # Devil's no floppy ear
    if traitStr[0] == "v" and TRAIT_ENCODINGS["hat"][traitStr[4]] == "FloppyEar":
        traitsDict["hat"].append(traitStr[4])
        traitStr = traitStr[0:4] + "_" + traitStr[5:]
    # No laughing eyes with caps
    if traitStr[5] == "g" and traitStr[4] in typesOfCaps:
        traitStr = traitStr[0:5] + "_"
    # No tongue out for skeletons
    if traitStr[3] == "q" and traitStr[0] == "s":
        traitStr = traitStr[0:3] + "_" + traitStr[4:]
    return traitStr

# Entry point
main()
