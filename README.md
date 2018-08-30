# mediagen
mediagen is a python program that generates files randomly in a variable folder structure for the purposes of generating test data. Mediagen creates text files, image files, and video files, organizing them in a random directory structure.  

My Use Case:
I'm testing a backup program that requires real files of various size, type, and date. I don't want to use real information for my testing. 

Here's how it works:

Mediagen takes:
- the size of the total desired dataset
- the range of file sizes
- a list of excluded file types (if any)
- the range of dates for the creation date of each file
 

----

How to Package: python setup.py sdist
