"""
Use to distribute photomurals to individual gNum folders
"""

import os

# Remember to change directory
oldDir = "/Volumes/3Projects/OVMM-OhioVetMem/04_GRAPHICS/01_GRAPHIC STUDIES/06_Production Design/x-Alcove BG/1-PS/Output/_CMYK"
os.chdir(oldDir)

for f in os.listdir(os.getcwd()):
    if f != ".DS_Store":
        gNum, theRest = f.split("_")

        newDir = os.path.join("/Volumes/3Projects/OVMM-OhioVetMem/04_GRAPHICS/01_GRAPHIC STUDIES/06_Production Design/x-Alcove BG/1-PS/Output", gNum, "_CMYK")

        if not os.path.exists(newDir):
            os.makedirs(newDir)

        oldPath = os.path.join(oldDir, f)
        newPath = os.path.join(newDir, f)

        os.rename(oldPath, newPath)
