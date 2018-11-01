import os
import sys
import random
import string
import time
import datetime

from util import util


class createtxt:
    """Creates a txt of random size and random modified date as fed by the parent mediagen package"""
    def __init__(self):
        print("Create a TXT Image")

    def txtnamegen(self):
        textname = ''.join([random.choice(string.ascii_letters) for n in range(16)])
        return textname

    def txtgen(self,filestruct,picx=300,picy=300):
        txtname = self.txtnamegen()
        print("txtname: ",txtname)
        print("txtpath: ",filestruct[0][0] )
        print("txtdate: ",filestruct[1][0] )
        print("txtpath: ",filestruct[2][0] )
        fullpath = ("%s/%s.%s") % (filestruct[0][0],txtname,filestruct[2][0])
        print("txt file fullpath: ", fullpath)
        txtfile = open(fullpath, "w")
        textlinecontent = ""
        textlinecontents = ""

        for l in range(random.randint(10,1000)):
            print("iterator: ",l) 
            textlinecontent = ''.join([random.choice(string.ascii_letters) for n in range(500)])
            textlinecontents = textlinecontents + "," + textlinecontent
            print("textlinecontent: ",textlinecontent)
            print("textlinecontents: ",textlinecontents)

        txtfile.writelines(str(textlinecontents))
        txtfile.close

        #Change MTime
        utime = time.mktime(filestruct[1][0].timetuple())
        os.utime(fullpath, (utime,utime))

        return fullpath
