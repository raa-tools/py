"""
--------------------------------------------------------
--------------------------------------------------------
 Compare 2 space-separated lists (e.g., character sets)
--------------------------------------------------------
--------------------------------------------------------

This script compares 2 space-separated lists from 2 text files and
writes the "difference" to a third text file (currently named "difference.txt").

Prior to running the script, remember to change paths & file names.
difference.txt will be created if no such file exists.
"""

import os

os.chdir("/Users/jesentanadi/Desktop/") # remember to change directory

with open("file1.txt", "rU") as rFile1: #.txt file of char set 1
    inputList1 = rFile1.read().split(" ")

with open("file2.txt", "rU") as rFile2: #.txt file of char set 2
    inputList2 = rFile2.read().split(" ")

#Writes result to file (new if file doesn't exist)
with open("difference.txt", "w") as wFile:

    #Goes through 1st list & compares with 2nd list
    wFile.write("In 1st char set:\n")
    for item in inputList1:
        if item not in inputList2:
            wFile.write(item + "\n")

    #Goes through 2nd list & compares with 1st list
    wFile.write("\n\nIn 2nd char set:\n")
    for item in inputList2:
        if item not in inputList1:
            wFile.write(item + "\n")

"""
---------------
     TO DO
---------------

+ "Open File" window to choose text files
+ Combine with space-separated script

"""
