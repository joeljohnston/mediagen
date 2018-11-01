import os
import sys
import numpy
from PIL import Image
import random
import string
import time
import datetime
import cv2
from util import util

class creatempg:
    """Creates a mpg of random size (number of frames) and random modified date as fed by the parent mediagen package"""
    def __init__(self):
        print("Create a JPG Image")

    def mpgnamegen(self):
        #Create a random name of the movie file
        moviename = ''.join([random.choice(string.ascii_letters) for n in range(16)])
        return moviename

    def mpggen(self,filestruct,frames,picx=300,picy=300):

        #instantiate a name
        mpgname = self.mpgnamegen()

        #print("mpgname: ",mpgname)
        #print("mpgpath: ",filestruct[0][0] )
        #print("mpgdate: ",filestruct[1][0] )
        #print("mpgpath: ",filestruct[2][0] )
        fullpath = ("%s/%s.%s") % (filestruct[0][0],mpgname,filestruct[2][0])
        print("mpg movie fullpath: ", fullpath)

        #create movie passing randomframes and target path
        self.makeVideo( frames, fullpath)

        #Set randomly assigned datetime to created file
        if os.path.isfile(fullpath):
            utime = time.mktime(filestruct[1][0].timetuple())
            os.utime(fullpath, (utime,utime))

    def makeVideo(self, inPattern, outFile):
        #e= None
        framelist = inPattern.split(",")
        fw= open( outFile, 'w' )

        pathlist = inPattern.split(",")
        frame = cv2.imread(pathlist[0])
        #cv2.imshow('video',frame)

        #grab movie dimensions from first frame (all frames should be consistent)
        if os.path.isfile(pathlist[0]):
            height, width, channels = frame.shape
        else:
            height=300
            width=300
            channels=1

        out = cv2.VideoWriter(outFile,cv2.VideoWriter_fourcc(*'mp4v'), 10, (width,height))

        for path in inPattern.split(","):
            print("frame: ", path)
            if os.path.isfile( path ):
                frame = cv2.imread(path)
                out.write(frame)
                #cv2.imshow('video',frame)
                if (cv2.waitKey(1) & 0xFF) == ord('q'):
                    break
            else:
              #print('%d frames written in %.2f secs( %.2f fps )' % ( i, time.time()- t, float( i )/ ( time.time()- t ) ))
                print("movie made")
        out.release()

        for dpath in inPattern.split(","):
            if os.path.isfile( dpath ):
                print("dpath: ",dpath)
                os.remove(dpath)

        #cv2.destroyAllWindows()
        print("The output video is {}".format(outFile))
