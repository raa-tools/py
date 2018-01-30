import os

os.chdir("/Users/jesentanadi/Desktop/imagetest/hi-res")

sourceFolder = "/Users/jesentanadi/Desktop/imagetest/original"

for targetItem in os.listdir(os.getcwd()):
    if targetItem != ".DS":
        targetName, targetExt = os.path.splitext(targetItem)

        for sourceItem in os.listdir(sourceFolder):
            if targetName in sourceItem:
                os.rename(targetItem, sourceItem)
