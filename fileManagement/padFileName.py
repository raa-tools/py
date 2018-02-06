"""
Use to "pad" a file name (add  string before or after).
"""

from __future__ import print_function
import os
import sys
from _lib.getInput import getInput


while True:
    print("\nPrepend or append some string to end of file name")
    print("Type 'x' anytime to quit")

    filePath = getInput("Specify path:")
    if filePath == "x":
        break

    preOrAppend = ""
    while preOrAppend != "p" and preOrAppend != "a" and preOrAppend != "x":
        preOrAppend = getInput("Type 'p' to prepend or 'a' to append:").lower()
    
    if preOrAppend == "x":
        break

    newString = getInput("String to add:")
    if newString == "x":
        break

    os.chdir(filePath)
    
    for f in os.listdir(os.getcwd()):
        if "." in f and f != ".DS_Store":

            if preOrAppend == "p":
                newName = newString + f
            
            elif preOrAppend == "a":
                fileName, fileExt = os.path.splitext(f)
                newName = fileName + newString + fileExt

            os.rename(f, newName)
