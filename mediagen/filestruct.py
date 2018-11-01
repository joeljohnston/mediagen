import sys
import os
import random
import time
from datetime import datetime

class filestruct:
    def structcrawl(self, _basedir):
        """Crawls the root filestructure of the base directory and renders an object with target filetypes"""
        d = 0
        dirstruct = []
        for root, dirs, files in os.walk(str(_basedir)):
           for d in dirs:
                directory = (root + '/' + d)
                dirstruct.append(directory)

        randomdir = random.choice(dirstruct)
        print("directory: ", randomdir)
        #randomdir = '/data/ingest/whatever'
        return randomdir

    def randomtype(self):
        filetypes = []
        filetypes.append("txt")
        filetypes.append("jpg")
        filetypes.append("png")
        filetypes.append("mp4")
        filetypes.append("mov")
        filetypes.append("bmp")
        filetypes.append("gif")

        randomfiletype = random.randint(0,len(filetypes)-1)
        return filetypes[randomfiletype]

    def randomdate(self,_daterangestart,_daterangeend,_dateformat,prop):
        """Creates a random datetime stamp from a provided range"""
        stime = time.mktime(time.strptime(str(_daterangestart), _dateformat))
        etime = time.mktime(time.strptime(str(_daterangeend), _dateformat))

        ptime = stime + prop * (etime - stime)
        print("timeint: ", int(ptime))
        dt_obj = datetime.fromtimestamp(ptime)
        print("ptime: ", dt_obj)

        return dt_obj
