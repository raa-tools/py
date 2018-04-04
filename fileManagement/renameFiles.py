"""
Generic file renaming
Works from CLI with args:
 - file dir
 - file extension
 - current string to replace
 - new string
"""

import os
import sys

def fixExt(ext):
    """ (str) -> str
    Prepend "." to extension if it doesn't start with one
    """
    if not ext.startswith("."):
        return ".{}".format(ext)
    return ext

def renameFiles(inputDir, inputExt, currentString, newString):
    """ (str, str, str, str) -> NoneType
    Renames files in inputDir with inputExt,
    replacing currentString with newString
    """
    os.chdir(inputDir)
    for f in os.listdir(os.getcwd()):
        if f != ".DS_Store":
            fileName, fileExt = os.path.splitext(f)

            if fileExt == fixExt(inputExt):
                fileName = fileName.replace(currentString, newString)

            newName = "{}{}".format(fileName, fileExt)
            os.rename(f, newName)

# Get arguments from CLI
print(sys.argv[0] + " running")
renameFiles(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
