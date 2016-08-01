#!/usr/bin/perl

#my %count;
while(<>){
	chomp;
	$count{$_}++ for (split);
}

while(($k, $v) = each (%count)){
	print "$k ==> $v\n";
}
