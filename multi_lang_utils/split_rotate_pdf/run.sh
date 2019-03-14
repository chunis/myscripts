#!/bin/bash

# About: 
#  1. for each pages of a PDF, split between the middle and becomes 2 pages
#  2. Rotate the bottom pages (even pages) to 180 degrees
#  3. Skip the first "start" pages (still split, but doesn't rotate)
#   So, for start = 2 (totally 6 pages):
#        |---------|---------|---------|---------|---------|---------|
#        | 1-- --1 | 1-- --1 | 1-- --1 | 1-- --1 | 1-- --1 | 1-- --1 |
#        |---------|---------|---------|---------|---------|---------|
#   The output would be like this (now totally 12 pages): 
#        |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
#        | 1-- | --1 | 1-- | --1 | 1-- | 1-- | 1-- | 1-- | 1-- | 1-- | 1-- | 1-- |
#        |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
#
# Need to install these tools first:
#   $ sudo pip install pypdf2
#   $ sudo apt install qpdf
#   And tool 'k2pdfopt' comes from: http://willus.com/k2pdfopt/
#
# Chunis Deng (chunchengfh@gmail.com)
# 2019.03.15


name=$1
root=$(echo $name | sed 's/\.pdf//')
out=$(echo $root | sed 's/raz_/cx_/')
start=3  # skip the first 0, 1, 2 totally 3 pages

if [ "$name" = "" ]; then
	echo "Usage: $0 xxx.pdf"
	exit
fi

echo -e "\n\n" | ./k2pdfopt -grid 1x2x2 -w 1s -h 0.5s -om 0.1s $name
tmpname=${root}_k2opt.pdf
#echo $tmpname

qpdf --password='' --decrypt $tmpname q.pdf
./rotate_pdf_pages.py q.pdf $out.pdf $start

rm $tmpname q.pdf
