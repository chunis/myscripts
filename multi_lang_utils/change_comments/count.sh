#!/bin/sh

# get file list which has embedded c comments
# usage: $0 <dir with c source code>

find $1 -name '*.[ch]' | while read f; do
	echo "$f:"
	echo "-------------------"
	get_embedded_comments.pl $f
done
