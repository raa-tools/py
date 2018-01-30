"""
Use to rename parsed script files in Combat 1 & Combat 2 to match panel codes
"""

import os

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Images/HIGH RESOLUTION IMAGES/NEW HIGH RES/New Folder With Items")

for f in os.listdir(os.getcwd()):
    if f != ".DS_Store":
        fileName, fileExt = os.path.splitext(f)

        if fileExt.lower() == ".jpg" or fileExt.lower() == ".jpeg":
            oldPath = os.path.join(os.getcwd(), f)
            newPath = os.path.join("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Images/HIGH RESOLUTION IMAGES/NEW HIGH RES/New Folder With Items/_JPGs", f)

            os.rename(oldPath, newPath)
