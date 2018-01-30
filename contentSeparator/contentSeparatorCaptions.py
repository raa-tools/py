import os
from collections import OrderedDict

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Thematic Displays/")

with open("_THCaptions.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

inputTextList = [text for text in inputTextList if text != "\n"]

codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

contentDict = {inputTextList[codeIndex[i]].replace("\n", "").split(" ")[0] :\
               inputTextList[codeIndex[i]+2:codeIndex[i+1]] for i in range(len(codeIndex)-1)}

contentDict = OrderedDict(sorted(contentDict.items()))

def combineCaptions():
    """
    Function to combine different captions across
    the same exhibit & topic

    Returns a new dictionary with Exhibit_Topic as key
    and all captions in that exhibit_topic as value
    """

    exhibitTopic, codeMemory = " ", " "
    newContentDict = {}

    for code in contentDict:

        # Check if we're still in the same exhibitTopic
        # If so, insert the contents of that key and the previous key to newContentDict
        # *** THIS NEEDS TO BE EDITED TO ACCOMMODATE CAPTIONS WITH MORE THAN 2 VALUES ***
        if exhibitTopic in code:
            newContentDict[exhibitTopic] = contentDict[code] + contentDict[codeMemory]

        # Assign the caption code we just dealt with to
        # a variable so we can add it to our newContentDict later
        codeMemory = code

        exhibit, topic, caption = code.split("_")
        exhibitTopic = "{}_{}".format(exhibit, topic)

    return newContentDict


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


combinedContent = combineCaptions()

for key in combinedContent:
    pathName = makeFolderName(key)
    makeFolder(str(pathName))

    bodyPath = os.path.join(pathName, key.upper() + "_CP.txt")

    with open(bodyPath, "w") as wBodyFile:
        for item in combinedContent[key]:
            wBodyFile.write(item + "\n")
