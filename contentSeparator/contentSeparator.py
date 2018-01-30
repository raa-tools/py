import os

# Remember to change directory
os.chdir("/Users/jesentanadi/Desktop/Ohio Test/Script")

with open("_TL_V.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

inputTextList = [text for text in inputTextList if text != "\n"]

codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

contentDict = {inputTextList[codeIndex[i]].replace("\n", "").split(" ")[0] : \
               inputTextList[codeIndex[i]+1:codeIndex[i+1]] \
               for i in range(len(codeIndex)-1)}

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
        return "{}/{}/".format(exhibit, topic.upper())


def makeFolder(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)

for key in contentDict:

    title = contentDict[key][0].replace("\n", "")
    body = contentDict[key][1:]

    pathName = makeFolderName(key)
    makeFolder(str(pathName))

    titlePath = os.path.join(pathName, key.upper() + "-T.txt")
    bodyPath = os.path.join(pathName, key.upper() + "-B.txt")

    with open(titlePath, "w") as wTitleFile:
        for item in title:
            wTitleFile.write(item)

    with open(bodyPath, "w") as wBodyFile:
        for item in body:
            wBodyFile.write(item)
