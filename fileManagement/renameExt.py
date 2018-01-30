"""
Use to rename extensions for uniformity in a dir.
Doesn't reformat file to new file type.
"""

import os
import sys
from __future__ import print_function

def checkExtension(newExt):
    """
    Makes sure there's a "." before extension name
    """
    return "." + newExt if "." not in newExt else newExt

def getPath():
    """
    Get path using 2 different input methods (Py 3.X vs 2.X)
    """
    return input("Specify path: ") if sys.version_info[0] >= 3 else raw_input("Specify path: ")

def getNewExt():
    """
    Get new ext using 2 different input methods (Py 3.X vs 2.X)
    """
    return checkExtension(input("New extension: ")) if sys.version_info[0] >= 3 \
                                                    else checkExtension(raw_input("New ext: "))

while True:
    print("\nRename extensions to make them uniform. This script doesn't reformat files!!!")
    print("Type 'x' to quit")

    filePath = getPath()

    if filePath.lower() == "x":
        break

    os.chdir(filePath)
    newExt = getNewExt()

    for f in os.listdir(os.getcwd()):
        if "." in f and f != ".DS_Store":
            fileName, fileExt = os.path.splitext(f)
            newName = fileName + newExt

            os.rename(f, newName)
