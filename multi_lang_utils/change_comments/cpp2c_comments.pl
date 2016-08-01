#!/usr/bin/perl

use strict;
use warnings;

$^I = ".bak";
while(<>){
	if(m{://}){ # skip something likes "cert://" or "http://"
		unless(/case/){ # don't skip "case xx://comment"
			print;
			next;
		}
	}
	if(m{/\*.*//}){ # likes "/* int a = 3; // xxx */"
		print;
		next;
	}
	if(m{//(.*)/\*}){ # likes "// int a = 3; /* a is an int */"
		s,//(.*)/\*,/*$1*/ /*,;
		print;
		next;
	}
	if(m{//.*\*/}){ # likes "// int a = 3; /* a is an int */"
		s,//,/*,;
		print;
		next;
	}
	if(m{^\s*//\s*$}){ # line with '//' and spaces only, so just delete it
		s{^.*$}{};
		print;
		next;
	}

	s,//(.*),/*$1 */,;
	print;
}
