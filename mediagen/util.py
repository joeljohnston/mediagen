import os
import time
import sys


class util:
    """ Utilities needed by a number of methods throughout """
    def setmtime(self, filestruct):
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
        os.utime(_fullpath,(atime,mtime))
