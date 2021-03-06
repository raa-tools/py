"""
--------------------------------------------------------
--------------------------------------------------------
 Compare 2 return-separated lists
--------------------------------------------------------
--------------------------------------------------------

This script compares 2 return-separated lists from 2 text files and
writes the "same" to a third text file (currently named "same.txt").

Prior to running the script, remember to change paths & file names.
difference.txt will be created if no such file exists.
"""

import os

os.chdir("/Users/jesentanadi/Desktop/") # remember to change directory

with open("1.txt", 'rU') as rFile1: #.txt file of char set 1
    inputList1 = rFile1.readlines() #Returns a list

with open("2.txt", 'rU') as rFile2: #.txt file of char set 2
    inputList2 = rFile2.readlines() #Returns a list

inputList1 = [item.lower() for item in inputList1]
inputList2 = [item.lower() for item in inputList2]


#Writes result to file (new if file doesn't exist)
with open("same.txt", "w") as wFile:

    #Removes extra line breaks and inserts list back into the same variable ("list comprehension")
    inputList1 = [item.replace("\n", "") for item in inputList1]
    inputList2 = [item.replace("\n", "") for item in inputList2]

    #Goes through 1st list & compares with 2nd list
    wFile.write("Repeating files:\n")
    for item in inputList1:
        if item in inputList2:
            wFile.write(item + "\n")

"""
---------------
     TO DO
---------------

+ "Open File" window to choose text files
+ Combine with space-separated script

"""
