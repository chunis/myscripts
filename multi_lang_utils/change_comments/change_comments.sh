#!/bin/sh

# Change codes to follow Linux code style.

if [ "$1" = "" ]; then
	echo "Usage: $0 <dirname with C source code>"
	echo
	exit
fi

# checks where we are
[ -f ./cpp2c_comments.pl ] && mydir="./"
[ -f ./spaces2tabs.pl ] && mydir="./"

find $1 -name '*.[ch]' | while read f; do
	# 1. convert EOF from dos to unix
	which fromdos > /dev/null && fromdos $f
	which dos2unix > /dev/null && dos2unix $f

	# 2. re-format to Linux code style
	./indent -npro -kr -i8 -ts8 -sob -l80 -ss -ncs -cp1 $f

	# 3. delete whitespaces from end of line
	sed -i 's/[ \t]\+$//' $f

	# 4. convert comments from // style to /* */ style
	${mydir}cpp2c_comments.pl $f

	# 5. convert each 8 leading spaces to a Table
	${mydir}spaces2tabs.pl $f

	rm -f $f.bak # remove backup files produced by perl scripts
	rm -f $f~ # remove backup files produced by indent
done
