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

            if inputExt == "all" or fileExt == fixExt(inputExt):
                fileName = fileName.replace(currentString, newString)

            newName = "{}{}".format(fileName, fileExt)
            os.rename(f, newName)



try:
    if sys.argv[1].lower() == "help" or sys.argv[1].lower() == "h":
        print("Signature: {} directory extension currentString newString".format(sys.argv[0]))
    else:
        renameFiles(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        print("Script running")
except IndexError:
    print("Nope! Did you type in the right number of args?")
    print("Type in '{} help' to see this script's signature".format(sys.argv[0]))
