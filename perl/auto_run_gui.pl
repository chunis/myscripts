#!/usr/bin/perl

# About: Repeatly move mouse and click it, this can stop the screen-locking 
# And I used this to automatically delete all of my >240000 LKML mails
# 
# Prepare:
# $ cpanm --installdeps X11::GUITest && cpanm X11::GUITest
#
# Chunis Deng (chunchengfh@gmail.com)


use strict;
use warnings;

use X11::GUITest qw/
	WaitSeconds ClickMouseButton M_RIGHT M_LEFT
	MoveMouseAbs
	/;

my $i = 0;
while($i < 900){
	MoveMouseAbs 230, 210;
	#ClickMouseButton M_RIGHT;
	ClickMouseButton M_LEFT;
	WaitSeconds(1);

	MoveMouseAbs 480, 210;
	ClickMouseButton M_LEFT;
	WaitSeconds(5);

	print "i = $i\n";
	$i++;
}
