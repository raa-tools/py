import os

# Remember to change directory
os.chdir("/Users/jesentanadi/Desktop/")

with open("test.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

inputTextList = [text for text in inputTextList if text != "\n"] #clear lines that are empty newlines

creditDict = {}
for inputText in inputTextList:
    gNum, credit = inputText.split("\t")
    creditDict[gNum] = credit

for key in creditDict:
    if creditDict[key][-1] == "\n":
        creditDict[key] = creditDict[key][:-1]

with open("processed.txt", "w") as wFile:
    for key in creditDict:
        wFile.write("{}\n{}\n".format(key, creditDict[key]))


# for key in contentDict:

#     title = contentDict[key][0].replace("\n", "")
#     body = contentDict[key][1:]

#     pathName = makeFolderName(key)
#     makeFolder(str(pathName))

#     titlePath = os.path.join(pathName, key.upper() + "-T.txt")
#     bodyPath = os.path.join(pathName, key.upper() + "-B.txt")

#     with open(titlePath, "w") as wTitleFile:
#         for item in title:
#             wTitleFile.write(item)

#     with open(bodyPath, "w") as wBodyFile:
#         for item in body:
#             wBodyFile.write(item)
