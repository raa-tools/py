from __future__ import print_function
import os
from collections import OrderedDict
import re
import io


def makeFolder(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)


# MAIN BELOW

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Timeline/")

with io.open("_TL_CAPS.txt", 'rU', encoding='utf8') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

with io.open("_TL_Credits.txt", 'rU', encoding='utf8') as readFile: #.txt file
    inputCreditList = readFile.readlines() #Returns a list    

# Clean up inputTextList: get rid of empty items (eg. only newlines and spaces & newline)
inputTextList = [text for text in inputTextList if text != "\n" and not re.match(r" +\n", text)]

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


# Iterate over contentDict to generate textblocks
# and write files
for key in contentDict:
    # Generate clean captions for per caption group
    captionBlock = ""
    if not capStarterDict[key]:
        captionBlock = contentDict[key][1] + "\n"

    elif len(capStarterDict[key]) < 2:
        for i in range(1, len(contentDict[key]) + 1, 2):
            captionBlock += contentDict[key][i]

        captionBlock += "\n"

    else:
        for i in range(len(capStarterDict[key]) - 1):
            start = capStarterDict[key][i]
            end = capStarterDict[key][i + 1]

            for j in range(start, end, 2):
                captionBlock += contentDict[key][j]

            captionBlock += "\n"

    

    # Generate a list of credits per caption group
    creditList = []
    for gNum in gNumDict[key]:
        try:
            creditList.append(creditDict[gNum.lower()])
        
        except KeyError:
            creditList.append(u"Missing credit for {}".format(gNum))
    
    # Generate semicolon-separated credits per caption group
    creditBlock = ("; ".join(creditList))
    

    # Finally write some files
    pathName = "TL/CAPS/"

    makeFolder(pathName)

    captionPath = os.path.join(pathName, key.upper() + ".txt")

    with io.open(captionPath, "w") as captionFile:
        captionFile.write(captionBlock)
        captionFile.write(creditBlock)