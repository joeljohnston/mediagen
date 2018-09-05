import os
import sys
import argparse

#import local classes
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dirstruct import dirstruct
from filestruct import filestruct

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
    parser.add_argument('--maxbasesubs', metavar='maxbasesubs', type=str, nargs='+', help='Maximum number of directories created in the top of the tree')
    args = parser.parse_args()

    #invoke dirstruct class to create the random base directory structure
    a = dirstruct(str(args.basedir[0]),args.dirdepth[0],args.maxbasesubs[0])

    #invoke the random file generation class to framework jobs
    b = filestruct()
if __name__ == '__main__':
    _launch()
