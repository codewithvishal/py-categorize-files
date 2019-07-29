import os, shutil

cwd = os.getcwd()
dir_files = os.listdir()

class Categorize():

    def __init__(self, **obj):
        self.path = cwd
        self.movedir = obj["movedir"]
        self.extension = obj["extension"]
        self.moveto()

    def moveto(self):
        total_file_moved = 0

        # to check if images, songs, videos, pdf dir is there if not then create a new one
        if not os.path.exists(os.path.join(self.path, self.movedir)):
            os.makedirs(os.path.join(self.path, self.movedir))
        
        # Now Move the file to their respctive directory
        for item in dir_files:
            item = item.lower()
            if os.path.isfile(item):
                if item.endswith(self.extension):
                    total_file_moved += 1
                    shutil.move(item, os.path.join(self.path, self.movedir))
        
        print({
            "Status": "Completed",
            "File is": self.movedir + "(" + self.extension + ")",
            "Total Files Moved": total_file_moved
        })


app = Categorize(**{
    "movedir": "images",
    "extension": "png"
    })
app = Categorize(**{
    "movedir": "images",
    "extension": "jpg"
    })
app = Categorize(**{
    "movedir": "videos",
    "extension": "mp4"
    })
app = Categorize(**{
    "movedir": "songs",
    "extension": "mp3"
    })
app = Categorize(**{
    "movedir": "docs",
    "extension": "pdf"
    })
app = Categorize(**{
    "movedir": "docs",
    "extension": "xlsx"
    })   
