import os
from collections import OrderedDict

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Timeline/")

with open("_TL_DL.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

inputTextList = [text for text in inputTextList if text != "\n"]

codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

contentDict = {inputTextList[codeIndex[i]].replace("\n", "").split(" ")[0] : \
               inputTextList[codeIndex[i]+1:codeIndex[i+1]] \
               for i in range(len(codeIndex)-1)}

contentDict = OrderedDict(sorted(contentDict.items()))

def makeFolderName(fileName):
    """
    Function to make folders based on file name
    Returns a path to be used by makeFolder() function

    Currently a little inconsistent with how it treats exhibits
    """

    exhibit, topic, story = fileName.split("_")

    if exhibit == "TH":
        return "{}/".format(exhibit)

    elif exhibit == "TL":
        return "{}/DL/".format(exhibit)


def makeFolder(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)


for key in contentDict:

    # Add a star to the beginning of vet entries ("A" in stars font)
    contentDict[key] = ["A " + entry if entry.endswith("[vet]\n") else entry for entry in contentDict[key]]

    pathName = makeFolderName(key)
    makeFolder(str(pathName))

    # Need files to be numbered consecutively, but for loop below has step of 2...
    fileNum = 1

    for i in range(0, len(contentDict[key]), 2):
        # Separate paths for text entry & date entry
        textPath = os.path.join(pathName, key.upper() + "-" + str(fileNum) + "T.txt")
        datePath = os.path.join(pathName, key.upper() + "-" + str(fileNum) + "D.txt")

        with open(textPath, "w") as wTextFile:
            wTextFile.write(contentDict[key][i])

        # Date entry is always the next index
        with open(datePath, "w") as wDateFile:
            wDateFile.write(contentDict[key][i + 1])

        fileNum += 1
