import os
import sys
import numpy
from PIL import Image
import random
import string
import time
import datetime

from util import util


class createjpg:
    """Creates a jpg of random size and random modified date as fed by the parent mediagen package"""
    def __init__(self):
        print("Create a JPG Image")

    def jpgnamegen(self):
        imagename = ''.join([random.choice(string.ascii_letters) for n in range(16)])
        return imagename

    def jpggen(self,filestruct,picx=300,picy=300):
        jpegname = self.jpgnamegen()
        print("jpegname: ",jpegname)
        print("jpegpath: ",filestruct[0][0] )
        print("jpegpath: ",filestruct[1][0] )
        print("jpegpath: ",filestruct[2][0] )
        fullpath = ("%s/%s.%s") % (filestruct[0][0],jpegname,filestruct[2][0])
        print("jpg image fullpath: ", fullpath)

        if picx == 0 or picy == 0:
            picx = random.randint(300,3890)
            picy = random.randint(200,2160)

        image = numpy.random.rand(picx,picy, 3) * 255
        image_out = Image.fromarray(image.astype('uint8')).convert('RGB')
        print("saving jpg to: ", fullpath)
        image_out.save(fullpath)

        print("raw: ", filestruct[1][0])

        #Change MTime
        self.util.setmtime(filestruct)

        return fullpath
