#!/usr/bin/perl

use strict;
use warnings;

my @lines = (<>);
my $content = join '', @lines;
my @cases;

#print $content;
@cases = ($content =~ m{(/\*.*?)\*/}smg);
for my $x (@cases){
	if($x =~ m{/\*.*/\*}sm){
		print "$x\n";
		print "-----------------\n\n";
	}
}
