#!/usr/bin/perl

use strict;
use warnings;

$^I = ".bak";
while(<>){
	while(/^\+\t* {8}/){
		s/ {8}/\t/;
	}
	print;
}
