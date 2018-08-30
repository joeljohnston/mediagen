import os
import sys
import time
import shutil
import random
import string

from glob import glob

class dirstruct:
    """ Builds the Directory structure randomly in the target directory """
    def __init__(self,basedir):
        #Make sure basedir exists
        if not os.path.exists(basedir):
            print("Your Base Directory %s doesn't seem to exist, shall I create it? " % (str(basedir)))
            basedir_create = input("(yes/no): ")
            if basedir_create == 'yes':
                os.makedirs(basedir)
            else:
                print("Sorry can't help you without a Base Directory")
                sys.exit()

        print(type(basedir))
        print("Base Directory %s exists" % (str(basedir)))
        self.gensubdir(str(basedir))

    def dirname(self):
        #Generate random name for directory
        randomdirname= ''.join([random.choice(string.ascii_letters) for n in range(16)])
        return randomdirname

    def createdirs(self,basedir,subdir):
        targetdir = str(basedir + subdir)
        os.makedirs(targetdir)

    def gensubdir(self,_basedir):
        for folder, subs, files in os.walk(_basedir):
            print("subs: ", subs)
            if not os.path.exists(str(subs)):
                thisdir = self.dirname()
                print("newdir: ",thisdir)
                #createdirs(basedir + '/' + thisdir)
                print("currentdir: ",folder)
                print("currentsubs: ",subs)
            else:
                newdir = subs + '/' + dirname()
                print("newsub: ", newdir)
                #createdirs(basedir + '/' + newdir)

#    for folder, subs, files in os.walk(fromdir):
#            with open(os.path.join(folder, 'python-outfile.txt'), 'w') as dest:
#                for filename in files:
#                    print "filename: ", filename
#                    ext = os.path.splitext(filename)[1][1:]
#                    newfile = os.path.splitext(filename)[0]
#                print "ext: ", ext
#                print "file: ", newfile
#                    newfilename = "%s.%s.%s" % (newfile, int((time.time() + 0.5) * 1000 ), ext)
#                    print "newfilename: ", newfilename
#                filepath = "%s/%s" % (folder,filename)
#                print "filepath: ", filepath
#                    ftime = time.gmtime(os.path.getmtime(filepath))
#                    ctime_dir = "%s/%s" % (str(ftime.tm_year), str(ftime.tm_mon))
#                    dest_dir="%s/%s" % (todir, ctime_dir)
#                    dest="%s/%s/%s" % (todir, ctime_dir, filename)
#                print "Destination Path: %s" % (dest)
#                newdest= "%s/%s" % (dest_dir, newfilename)
#                print "newdest: ", newdest
#                if not os.path.exists(dest_dir):
#                        os.makedirs(dest_dir)
#                    if not os.path.exists(dest):
#                    shutil.move(filepath, dest)
#                else:
#                    shutil.move(filepath, newdest)
