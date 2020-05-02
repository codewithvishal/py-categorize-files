# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.
# Don't use this code. I am still working on it rather use version 1.

import os, shutil
import time
import numpy

class Categorize():

    def __init__(self):
        # constructor var and functions
        self.createDirectory = ["Images", "Videos", "Songs", "Docs", "PY", "Others"]
        self.getFiles = os.listdir()
        self.path = os.getcwd()
        self.autoMode()
        
    def fileNewName(self, item):
        item_new_name = item.split(".")
        item_new_name.insert(1, str(int(time.time())))
        item_new_name.insert(2, ".")
        item_new_name = "".join(item_new_name)
        return item_new_name

    # autoMode Algorithm
    def autoMode(self):
        duplicates = {}
        img_tuple = ["img", "jpg", "png"]
        videos_tuple = ["3gp", "mp4", "avi", "wmv"]
        docs_tuple = ["pdf", "docs", "xlsx", "xlx", "xlsm", "csv", "xls"]
        songs_tuple = ["mp3"]
        i = 0
        j = 0
        k = 0
        l = 0
        # create directory
        # common directory
        for item in self.createDirectory:
            file = os.path.join(self.path, item)
            if not os.path.exists(file):
                os.makedirs(file)
            
        # First check if the file is already exists in the destination or have similar name
        # To check if the item is file, not directory
        for item in self.getFiles:
            item = item.lower()
            if not os.path.isdir(item): # Item must be a file, not directory
                # First check the file is not exists or have similar name in the destination directory

                # check which type of file it is
                if item.endswith(tuple(img_tuple)):
                    try:
                        shutil.move(item, "Images")
                    except:
                        i += 1
                        duplicates["images"] = "Total Duplicate Images Are {}".format(i)

                # videos
                if item.endswith(tuple(videos_tuple)):
                    try:
                        shutil.move(item, "Videos")
                    except:
                        j += 1
                        duplicates["videos"] = "Total Duplicate Videos Are {}".format(j)

                # videos
                if item.endswith(tuple(docs_tuple)):
                    try:
                        shutil.move(item, "docs")
                    except:
                        j += 1
                        duplicates["docs"] = "Total Duplicate Documents Are {}".format(k)
                    
                # videos
                if item.endswith(tuple(songs_tuple)):
                    try:
                        shutil.move(item, "Songs")
                    except:
                        j += 1
                        duplicates["songs"] = "Total Duplicate Songs Are {}".format(l)
            
        print(duplicates)

Categorize()
