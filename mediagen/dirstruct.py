import os
import sys
import random
import string

from glob import glob

class dirstruct:
    """ Builds the Directory structure randomly in the target directory """
    def __init__(self,basedir,_dirdepth,_maxbasesubs):
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
        randmaxrangesubs = random.randint(0,int(_maxbasesubs))
        for i in range(random.randint(1,randmaxrangesubs)):
            self.gensubdir(str(basedir),_dirdepth)
            self.list_files(str(basedir))

    def dirname(self):
        #Generate random name for directory
        randomdirname= ''.join([random.choice(string.ascii_letters) for n in range(16)])
        return randomdirname

    def createdirs(self,targetdir):
        os.makedirs(targetdir)

    def list_files(self, startpath):
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            #print("level: ", level)
            indent = ' ' * 4 * (level)
            #print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    def gensubdir2(self,_basedir):
        for root, dirs, files in os.walk(_basedir):
            print("dirs: ", dirs)

    def gensubdir(self,_basedir, _dirdepth):
        i = 0
        j = 0
        sub_path = _basedir
        for folder, subs, files in os.walk(_basedir):
            #print("number of subs: ", len(subs))
            _dirarray = []
            #randomdir = random.randint(1,len(subs))
            while i < random.randint(0,int(_dirdepth)):
                _dirarray.append(self.dirname())
                i = i + 1
            while j < random.randint(0,len(_dirarray)):
                sub_path = (sub_path + '/' + _dirarray[j])
                j = j + 1
                print("sub_path: ", sub_path)
            if not os.path.exists(sub_path):
                self.createdirs(sub_path)
