from __future__ import print_function
import os
import sys


def main(directory, fileToOpen):
    """
    Main function that separates content

    Uses a couple of helper functions
    Takes in directory & file to open as params
    """
    os.chdir(directory)

    with open(fileToOpen, 'rU') as readFile: #.txt file
        inputTextList = readFile.readlines() #Returns a list

    inputTextList = [text for text in inputTextList if text != "\n"]

    codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
    codeIndex.append(len(inputTextList))

    contentDict = {inputTextList[codeIndex[i]].replace("\n", "").split(" ")[0] : \
                   inputTextList[codeIndex[i]+1:codeIndex[i+1]] \
                   for i in range(len(codeIndex)-1)}

    for key in contentDict:
        pathName = makeFolderName(key)
        makeFolder(pathName)
        
        title = contentDict[key][0].replace("\n", "")

        # Exhibit titles don't have body copy
        if "ti" in key.split("_")[2]:
            titlePath = os.path.join(pathName, key.upper() + ".txt")

        # Everything else is separated into a story title & story body file
        else:
            body = contentDict[key][1:]

            titlePath = os.path.join(pathName, key.upper() + "-T.txt")
            bodyPath = os.path.join(pathName, key.upper() + "-B.txt")

            # Write body file
            writeFile(bodyPath, body)

        # Write title file.
        writeFile(titlePath, title)


def writeFile(pathToFile, itemsInFile):
    with open(pathToFile, "w") as wFile:
        for item in itemsInFile:
            wFile.write(item)
        
        # Report back file name from pathToFile
        print("File {} written".format(os.path.basename(pathToFile)))

# Helper functions
def getPath():
    """
    Get path using 2 different input methods (Py 3.X vs 2.X)
    """
    return input("Specify path: ") if sys.version_info[0] >= 3 else raw_input("Specify path: ")


def getFileName():
    """
    Get path using 2 different input methods (Py 3.X vs 2.X)
    """
    return input("File name: ") if sys.version_info[0] >= 3 else raw_input("File name: ")


def readFile(workingDir, fileName):
    """
    Check if file name the user input exists or not
    """
    if not os.path.exists(os.path.join(workingDir, fileName)):
        print("File doesn't exist")
    
    else:
        main(workingDir, fileName)


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
        return "{}/NC/".format(exhibit)


def makeFolder(folderPath):
    """
    Simple function to make folder if it doesn't exist

    Input is the folder's path
    """
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)


# Portion that runs the functions below
while True:
    print("------------------------------------")
    print("Separate a big .txt file into parts.\nSome stuff still specific to NVMM.\n")
    print('Enter "x" at anytime to quit.')
    print("------------------------------------")
    workingDir = getPath()
    
    if workingDir == "x":
        break

    fileName = getFileName()

    if fileName == "x":
        break

    readFile(workingDir, fileName)
