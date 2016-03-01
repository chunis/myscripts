#!/bin/sh

# Chunis Deng (chunchengfh@gmail.com)
#
# About: Look up word from dict.cn


wget http://dict.cn/$1 -O /tmp/$1.html
w3m /tmp/$1.html
rm -f /tmp/$1.html
