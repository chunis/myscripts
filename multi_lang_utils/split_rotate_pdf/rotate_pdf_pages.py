#!/usr/bin/python

# Note: Rotate up down every even pages of a pdf file, start from page Nth.


import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


iname = sys.argv[1]
oname = sys.argv[2]
if len(sys.argv) > 3:
    start = int(sys.argv[3])
else:
    start = 3

print "Read from '%s', write to '%s', start from page %d" %(iname, oname, start)


src = PdfFileReader(open(iname, "rb"))
dst = PdfFileWriter()
pages = src.getNumPages()
print "pages: ", pages

for i in range(start):
    dst.addPage(src.getPage(i))

for i in range(start, pages):
    if i % 2:
        # dst.addPage(src.getPage(i).rotateCounterClockwise(180))
        dst.addPage(src.getPage(i).rotateClockwise(180))
    else:
        dst.addPage(src.getPage(i))

outputStream = file(oname, "wb")
dst.write(outputStream)
outputStream.close()

