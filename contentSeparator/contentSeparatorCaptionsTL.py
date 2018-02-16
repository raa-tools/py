from __future__ import print_function
import os
from collections import OrderedDict
import re


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

# Clean up inputTextList: get rid of empty items (eg. only newlines and spaces & newline)
inputTextList = [text for text in inputTextList if text != "\n" and not re.match(r" +\n", text)]

# Generate a list of where content codes appear
codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

# creditDict is {gNumber : credit}
creditDict = {item.split("\t")[0] : item.split("\t")[1] for item in inputCreditList}

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

# Empty this file
# comboText = "_TL_CAPS_combo.txt"
# with open(comboText, "w+") as comboFile:
#     comboFile.write("")

# Iterate over contentDict to generate textblocks
# and write files
for key in contentDict:
    capStarters = capStarterDict[key]
    gNums = gNumDict[key]

    # Generate clean captions for per caption group
    captionBlock = ""
    if not capStarters:
        captionBlock = contentDict[key][1] #+ "\n"

    elif len(capStarters) < 2:
        for i in range(1, len(contentDict[key]) + 1, 2):
            captionBlock += contentDict[key][i] #+ "\n"

        # captionBlock += "\n"

    else:
        for i in range(len(capStarters)):
            start = capStarters[i]

            # Quick fix to circumvent IndexError (when end = i+1)
            if capStarters[i] == capStarters[-1]:
                end = len(contentDict[key])
            else:
                end = capStarters[i + 1]

            for j in range(start, end, 2):
                captionBlock += contentDict[key][j] #+ "\n"

            # captionBlock += "\n"
    
    # Generate a list of credits per caption group
    creditList = []
    for gNum in gNumDict[key]:
        try:
            creditList.append(creditDict[gNum.lower()])
        
        except KeyError:
            creditList.append("Missing credit for {}".format(gNum))
    
    # Get rid of credits that end in and empty space & strip quote marks
    creditList = [credit[:-1].strip('"') if credit[-1] == " " else credit.strip('"') for credit in creditList]

    # Generate semicolon-separated credits per caption group
    creditBlock = ("; ".join(creditList))


    # Finally write some files
    pathName = "TL/CAPS/"

    makeFolder(pathName)

    captionPath = os.path.join(pathName, key.upper() + ".txt")

    with open(captionPath, "w") as captionFile:
        captionFile.write(captionBlock)
        captionFile.write("\n" + creditBlock)


    # Append to combo file:
    # with open(comboText, "a+") as comboFile:
    #     comboFile.write("------------\n" + key.upper() + "\n------------\n\n")
    #     comboFile.write(", ".join(gNums) + "\n\n\n")
    #     comboFile.write(captionBlock + "----------\n\n")
    #     comboFile.write(creditBlock)
    #     comboFile.write("\n\n------------------------------------------------------------\n\n")

    # print("File {}.txt written".format(key))
    