#!/usr/bin/python

# Chunis Deng (chunchengfh@gmail.com)
#
# About: rename file to its unquoted name, such as:
#	Face%20Detection%20and%20Recognition.pdf  ==>
#	Face Detection and Recognition.pdf
# Usage:
#	$0 -f <filename>  # for a single file
#	$0 -d <dirname>   # for a whole directory


import os, sys
import urllib


def rename_file(filename):
	if not os.path.exists(filename):
		print "WARNing! file '%s' doesn't exist!" %filename
		return
	if not os.path.isfile(filename):
		print "WARNing! '%s' isn't a regular file!" %filename
		return

	newname = urllib.unquote(filename)
	try:
		if newname != filename:
			os.rename(filename, newname)
	except:
		print "WARNing! Rename '%s' to '%s' failed" %(filename, newname)


def rename_dir(dirname):
	if not os.path.exists(dirname):
		print "WARNing! path '%s' doesn't exist!" %dirname
		return
	if not os.path.isdir(dirname):
		print "WARNing! '%s' isn't a dir!" %dirname
		return

	for filename in os.listdir(dirname):
		newname = urllib.unquote(filename)
		try:
			if newname != filename:
				os.rename(os.path.join(dirname, filename),
					os.path.join(dirname, newname))
		except:
			print "WARNing! Rename '%s' to '%s' failed" %(filename, newname)

def usage():
	print ("Usage:\n%s -f <filename>\n%s -d <dirname>"
			%(sys.argv[0], sys.argv[0]))
	sys.exit()

if __name__ == '__main__':
	if len(sys.argv) < 3:
		usage()

	option, args = sys.argv[1:3]
	if option == '-f':
		rename_file(args)
	elif option == '-d':
		rename_dir(args)
	else:
		usage()

