import os
import sys
import numpy
from PIL import Image
import random
import string
import time
import datetime
import pymedia.video.vcodec as vcodec
import pygame
from util import util

class creatempg:
    """Creates a mpg of random size and random modified date as fed by the parent mediagen package"""
    def __init__(self):
        print("Create a JPG Image")

    def mpgnamegen(self):
        moviename = ''.join([random.choice(string.ascii_letters) for n in range(16)])
        return moviename

    def mpggen(self,filestruct,picx=300,picy=300):
        mpgname = self.mpgnamegen()
        print("mpgname: ",jpegname)
        print("mpgpath: ",filestruct[0][0] )
        print("mpgpath: ",filestruct[1][0] )
        print("mpgpath: ",filestruct[2][0] )
        fullpath = ("%s/%s.%s") % (filestruct[0][0],mpgname,filestruct[2][0])
        print("mpg movie fullpath: ", fullpath)

        numframes = random.randomint(300, 1800)

        makejpg = self.createjpg(dirstruct, 300, 300) 

        makeVideo( makejpg, fullpath, 'mpeg1video')

        #Change mtime on movie
        self.util.setmtime(filestruct)

    def makeVideo( inPattern, outFile, outCodec ):
        # Get video stream dimensions from the image size
        pygame.init()
        i= 1
        # Opening mpeg file for output
        e= None
        i= 1
        fw= open( outFile, 'wb' )
        while i:
            if os.path.isfile( inPattern % i ):
              s= pygame.image.load( inPattern % i )
              if not e:
                if outCodec== 'mpeg1video':
                  bitrate= 2700000
                else:
                  bitrate= 9800000

                params= { \
                  'type': 0,
                  'gop_size': 12,
                  'frame_rate_base': 125,
                  'max_b_frames': 0,
                  'height': s.get_height(),
                  'width': s.get_width(),
                  'frame_rate': 2997,
                  'deinterlace': 0,
                  'bitrate': bitrate,
                  'id': vcodec.getCodecID( outCodec )
                }
                print('Setting codec to' , params)
                e= vcodec.Encoder( params )
                t= time.time()

              # Create VFrame

              ss= pygame.image.tostring(s, "RGB")
              bmpFrame= vcodec.VFrame( vcodec.formats.PIX_FMT_RGB24, s.get_size(), (ss,None,None))
              yuvFrame= bmpFrame.convert( vcodec.formats.PIX_FMT_YUV420P )
              d= e.encode( yuvFrame )
              fw.write( d )
              i+= 1
            else:
              print('%d frames written in %.2f secs( %.2f fps )' % ( i, time.time()- t, float( i )/ ( time.time()- t ) ))
              i= 0

        fw.close()
        pygame.quit()
