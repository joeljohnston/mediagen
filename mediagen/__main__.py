import os
import sys
import argparse
import random
import datetime

#import local classes
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dirstruct import dirstruct
from filestruct import filestruct
from createjpg import createjpg 
from creatempg import creatempg
from createtxt import createtxt

def _launch():
    #Gather arguments from cli 
    parser = argparse.ArgumentParser(description='Generate Media')
    parser.add_argument('--basedir', metavar='basedir', type=str, nargs='+', help='Directory to start generating data in')
    parser.add_argument('--mediasize', metavar='mediasize', type=int, nargs='+', help='Total Sum of media to generate in GB')
    parser.add_argument('--filesizemin', metavar='filesizemin', type=int, nargs='+', help='Minimum file size to generate in GB')
    parser.add_argument('--filesizemax', metavar='filesizemax', type=int, nargs='+', help='Maximum file size to generate in GB')
    parser.add_argument('--excludetypes', metavar='excludetypes', type=str, nargs='+', help='Filetypes you dont want to generate')
    parser.add_argument('--daterangestart', metavar='daterangestart', type=str, nargs='+', help='Start Date of file creation daterange')
    parser.add_argument('--daterangeend', metavar='daterangeend', type=str, nargs='+', help='End Date of file creation daterange')
    parser.add_argument('--dirdepth', metavar='dirdepth', type=str, nargs='+', help='Number of directories down to create')
    parser.add_argument('--maxbasesubs', metavar='maxbasesubs', type=int, nargs='+', help='Maximum number of directories created in the top of the tree')
    parser.add_argument('--maxnumfiles', metavar='maxnumfiles', type=int, nargs='+', help='Maximum number of files created in the top of the tree')
    args = parser.parse_args()

    filestructure = []

    #invoke dirstruct class to create the random base directory structure
    a = dirstruct(str(args.basedir[0]),args.dirdepth[0],args.maxbasesubs[0])

    #invoke the random file generation class to framework jobs
    b = filestruct()

    #set vars for building a random filestructure
    i = 0
    j = 0
    k = 0
    now = datetime.datetime.now()
    #loop through the maxnumfiles argument to create a structure that represents a random sampling of filetypes across the directory structure
    while i in range(args.maxnumfiles[0]):
        fstructtype = b.randomtype()
        fstructdate = b.randomdate(args.daterangestart[0], args.daterangeend[0], '%Y-%m-%d', random.random())
        fstructpath = b.structcrawl(args.basedir[0])
        fileinfo = [[fstructpath],[fstructdate],[fstructtype]]
        filestructure.append(fileinfo)
        i = i + 1

    for j in filestructure:
        print(j[2][0])
        #if the selected filetype is jpg
        if j[2][0] == 'jpg':
            c = createjpg()
            c.jpggen(j,0,0)
        #if the selected filetype is mp4
        if j[2][0] == 'mp4':
            #we need to create the movie frames before handing of a list to the movie create function
            framestruct = []
            numframes = random.randint(500, 1800)
            #today = now.strftime("%Y-%m-%d %H:%M")
            today = j[1][0]
            frames = ""
            print("numframes: ",numframes)
            print("k: ",k)
            while k in range(numframes):
                framename = j[0][0].split("/")
                print("today: ", today)
                print("k: ", k)
                print("framename: ", framename[3])
                frameinfo = [['/tmp', [framename[3] + str(k)]],[today],['jpg']]
                framestruct.append(frameinfo)
                c = createjpg()
                print("framestruct: ", len(framestruct) )
                k = k + 1
            k = 0
            for l in framestruct:
                frames = c.jpggen(l,768,1080) + "," + frames

            print("frames: ", frames)
            m = creatempg()
            m.mpggen(j,frames)
        #if the selected filetype is txt
        if j[2][0] == 'txt':
            t = createtxt()
            t.txtgen(j)

if __name__ == '__main__':
    _launch()
