import os

os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Images/HIGH RESOLUTION IMAGES")


for item in os.listdir(os.getcwd()):
    if item != ".DS":
        fName, fExt = os.path.splitext(item)

        if "_" in fName:
            gNum, miscInfo = fName.split("_")
            os.rename(item, gNum+fExt)
    