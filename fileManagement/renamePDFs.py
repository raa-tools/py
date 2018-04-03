import os
import sys

# Remember to change directory
os.chdir(sys.argv[1])

for f in os.listdir(os.getcwd()):
    if f != ".DS_Store":
        fileName, fileExt = os.path.splitext(f)

        if fileExt == ".pdf":
            fileName = fileName.replace(".indd", "")

        newName = "{}{}".format(fileName, fileExt)

        os.rename(f, newName)
