from __future__ import print_function
import os
import sys


def main(directory, fileToOpen, outputSubDir):
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
        pathName = makeFolderName(key, outputSubDir)
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


# Helper functions
def getInput(prompt):
    """
    Return user input using 2 different methods (Py 3.X vs 2.X)
    """
    return input("{} ".format(prompt)) if sys.version_info[0] >= 3 else raw_input("{} ".format(prompt))


def makeFolderName(fileName, subDir):
    """
    Function to make generate folder name based on file name
    Path is exhibitCode/userDefinedSubfolder
    """

    exhibit, topic, story = fileName.split("_")

    return "{}/{}/".format(exhibit, subDir)


def makeFolder(folderPath):
    """
    Simple function to make folder if it doesn't exist

    Input is the folder's path
    """
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)


def writeFile(pathToFile, itemsInFile):
    with open(pathToFile, "w") as wFile:
        for item in itemsInFile:
            wFile.write(item)
        
        # Report back file name from pathToFile
        print("File {} written".format(os.path.basename(pathToFile)))


# Portion that runs the functions
while True:
    workingDir, fileName = "", " "

    print("\n------------------------------------")
    print("Separate a big .txt file into parts.")
    print("Some stuff still specific to NVMM.\n")
    print('Enter "x" at anytime to quit.')
    print("------------------------------------")

    # Get path from user
    while workingDir != "x" and not os.path.exists(workingDir):
        workingDir = getInput("Specify path:")

    if workingDir == "x":
        break

    # Get filename from user
    while fileName != "x" and not os.path.exists(os.path.join(workingDir, fileName)):
        fileName = getInput("File name:")

    if fileName == "x":
        break

    # Let user specify subfolder
    subFolder = getInput("Output subfolder (press enter for none):")
    if subFolder == "x":
        break

    main(workingDir, fileName, subFolder)
