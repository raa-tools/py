from __future__ import print_function
import os
from collections import OrderedDict
import re

def makeFolderName(fileName):
    """
    Function to make folders based on file name
    Returns a path to be used by makeFolder() function

    Currently a little inconsistent with how it treats exhibits
    """

    exhibit, topic = fileName.split("_")

    if exhibit == "TH":
        return "{}/CAPTION/".format(exhibit)

    elif exhibit == "TL":
        return "{}/{}/".format(exhibit, topic.upper())


def makeFolder(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)


# MAIN BELOW

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Timeline/")

with open("_TL_CAPS.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

with open("_TL_Credits.txt", 'rU') as readFile: #.txt file
    inputCreditList = readFile.readlines() #Returns a list    

inputTextList = [text for text in inputTextList if text != "\n"]

# Generate a list of where content codes appear
codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

# creditDict is {gNumber : credit}
creditDict = {item.split(",")[0] : item.split(",")[1] for item in inputCreditList}

# contentDict is {content code : list of captions}
contentDict = {inputTextList[codeIndex[i]].replace("\n", "").split(" ")[0] :\
               inputTextList[codeIndex[i]+1:codeIndex[i+1]] for i in range(len(codeIndex)-1)}

contentDict = OrderedDict(sorted(contentDict.items()))

gNumDict = {}
capStarterDict = {}

# Generate a dict of gNums and a dict of cap starter indices
# gNumDict is {content code : list of gNums}
# capStarterDict is {content code : list of indices}
for key in contentDict:
    gNumList = []
    capStarterIndex = []

    for index, item in enumerate(contentDict[key]):
        # This is g number: log it 
        if re.match(r"g\d+", item.lower()):
            gNumList.append(item[0:5]) # Don't include trailing newspace
    
        # This is caption starter: log its place
        elif "    " in item:
            capStarterIndex.append(index)
    
    gNumDict[key] = gNumList
    capStarterDict[key] = capStarterIndex

gNumDict = OrderedDict(sorted(gNumDict.items()))
capStarterDict = OrderedDict(sorted(capStarterDict.items()))

# Get rid of newlines in credits
for key in creditDict:
    if creditDict[key][-1] == "\n":
        creditDict[key] = creditDict[key][0:-1]


for key in contentDict:
    creditList = [creditDict[gNum] for gNum in gNumDict[key]]
    creditString = ("; ".join(creditList))

# combinedContent = combineCaptions()



# for key in combinedContent:
#     pathName = makeFolderName(key)
#     makeFolder(str(pathName))

#     bodyPath = os.path.join(pathName, key.upper() + "_CP.txt")

#     with open(bodyPath, "w") as wBodyFile:
#         for item in combinedContent[key]:
#             wBodyFile.write(item + "\n")
