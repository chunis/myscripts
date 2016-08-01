#!/usr/bin/awk -f

{
	for (i=1; i<=NF; i++) {
		count[$i] += 1
	}
}

END{
	for (i in count){
		print i, "==>", count[i]
	}
}
