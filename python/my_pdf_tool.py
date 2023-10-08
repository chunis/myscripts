#!/usr/bin/python3
# Chunis Deng (chunchengfh@gmail.com)

# usage: ./my_pdf_tool.py a.pdf:1,2,4-8,9:1 b.pdf::3 c.pdf -n 2 -o myoutput.pdf
#   input format: <pdf name>:<pages,pages_range>:<rotate>
#             -n: how many pages shrink to the same page


import os
import sys
from pypdf import PdfWriter, PdfReader


outname = "output.pdf"
n = 1
files = []

def process_inputs(f):
    print(f"f = {f}")
    items = f.split(":")
    name = items[0]
    if not os.path.exists(name):
        print(f"WARNING: file '{name}' doesn't exist. Ignore")
        return

    pages = 0
    rotate = 0
    if len(items) >= 2:
        pages = items[1]
    if len(items) >= 3:
        rotate = int(items[2]) % 4
    if len(items) >= 4:
        print(f"WARNING: too many items in '{f}'.")

    # process pages
    if pages != 0:
        pgs = pages.split(',')
        pages = []
        if pgs == []:
            pages.append(0)
        for x in pgs:
            if x == '':
                pages.append(0)
            elif len(x.split('-')) == 1:
                print('xxx = %s' %x)
                pages.append(int(x))
            elif len(x.split('-')) > 2:
                print("WARNING: pages format '%s' wrong." %x)
                return
            else:  # pages range
                x, y = x.split('-')
                pages.extend(range(int(x), int(y)+1))

    files.append([name, pages, rotate])



args = list(range(1, len(sys.argv)))
while args:
    i = args.pop(0)
    if sys.argv[i] == '-n':
        n = int(sys.argv[i+1])
        args.pop(0)
    elif sys.argv[i] == '-o':
        outname = sys.argv[i+1]
        args.pop(0)
    else:
        process_inputs(sys.argv[i])


print("Output name: --> %s" %outname)
if os.path.exists(outname):
    reply = input("file '%s' exists. Overwrite? [N] " %outname)
    if reply == '' or reply.lower()[0] == 'n':
        print("please provide output name and try again...\n")
        sys.exit()


output = PdfWriter()
for f in files:
    [name, pages, rt] = f

    inputfile = PdfReader(open(name, "rb"))
    if pages == 0:
        pages = range(len(inputfile.pages))

    for pg in pages:
        if rt == 0:
            output.add_page(inputfile.pages[pg])
        else:
            output.add_page(inputfile.pages[pg].rotate(90*rt))


'''
input1 = PdfReader(open(sys.argv[1], "rb"))
output.add_page(input1.pages[2])
output.add_page(input1.pages[3])
output.add_page(input1.pages[4].rotate(90))
#output.add_page(input1.pages[4])
output.add_page(input1.pages[5])
'''

outputStream = open(outname, "wb")
output.write(outputStream)
outputStream.close()


if n != 1:
    try:
        from pdfnup import generateNup
        generateNup(outname, n)
    except:
        print("WARNING: import 'pdfnup' failed, no re-layout be done")
