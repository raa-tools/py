"""
Use to rename parsed script files in Combat 1 & Combat 2 to match panel codes
"""

import os

# Remember to change directory
os.chdir("/Users/jesentanadi/Desktop/Ohio Test/Image/-")

for f in os.listdir(os.getcwd()):
    if f != ".DS_Store":
        fileName, fileExt = os.path.splitext(f)

        exhibit, topic, story = fileName.split("_")

        if story[2:4] == "01":
            topic = "EX10A"

        elif story[2:4] == "02":
            topic = "EX10B"
            story = story.replace("02", "01")

        newName = "{}_{}_{}{}".format(exhibit, topic, story, fileExt)

        os.rename(f, newName)
