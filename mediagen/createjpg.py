import os
import sys
import numpy
from PIL import Image
import random
import string
import time
import datetime


class createjpg:
    """Creates a jpg of random size and random modified date as fed by the parent mediagen package"""
    def __init__(self):
        print("Create a JPG Image")

    def jpgnamegen(self):
        imagename = ''.join([random.choice(string.ascii_letters) for n in range(16)])
        return imagename

    def jpggen(self,filestruct):
        jpegname = self.jpgnamegen()
        print("jpegname: ",jpegname)
        print("jpegpath: ",filestruct[0][0] )
        print("jpegpath: ",filestruct[1][0] )
        print("jpegpath: ",filestruct[2][0] )
        fullpath = ("%s/%s.%s") % (filestruct[0][0],jpegname,filestruct[2][0])
        print("jpg image fullpath: ", fullpath)

        image = numpy.random.rand(300, 300, 3) * 255
        image_out = Image.fromarray(image.astype('uint8')).convert('RGB')
        print("saving jpg to: ", fullpath)
        image_out.save(fullpath)

        print("raw: ", filestruct[1][0])
        dataconcat = str(filestruct[1][0])

        date = dataconcat.split("-",2)

        print("year: ", date[0])
        print("month: ", date[1])
        print("day: ", date[2])


        d = datetime.date(int(date[0]),int(date[1]),int(date[2]))
        unixtime = time.mktime(d.timetuple())

        #modify the file's mtime
        atime = unixtime 
        mtime = unixtime 
        os.utime(fullpath,(atime,mtime))
