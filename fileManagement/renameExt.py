"""
Use to rename extensions for uniformity in a dir.
Doesn't reformat file to new file type.
"""

from __future__ import print_function
import os
import sys
from _lib.getInput import getInput

def checkExtension(newExt):
    """
    Makes sure there's a "." before extension name
    """
    return "." + newExt if "." not in newExt else newExt


while True:
    print("\nRename extensions to make them uniform. This script doesn't reformat files!!!")
    print("Type 'x' to quit")

    filePath = getInput("Specify path:")
    if filePath == "x":
        break

    newExt = checkExtension(getInput("New extension:"))
    if newExt == "x":
        break

    os.chdir(filePath)
    
    for f in os.listdir(os.getcwd()):
        if os.path.splitext(f)[1] != newExt and "." in f and f != ".DS_Store":
            fileName, fileExt = os.path.splitext(f)
            newName = fileName + newExt

            os.rename(f, newName)
