#!/bin/sh

# Dennis Deng (ddeng@semtech.com)

output=$(sudo nmap -sP 192.168.1.1/24)
own_ip=$(ifconfig eno1 | /bin/grep -w 'inet' | awk '{ print $2 }')
ips=$(echo "$output" | grep 'Nmap scan report' | sed 's/.*for //' | grep -v $own_ip)
machost=$(echo "$output" | grep 'MAC Address: ' | sed 's/MAC Address: //' | sed 's/)$//')
macs=$(echo "$machost" | awk -F" \(" '{print $1}')
hosts=$(echo "$machost" | awk -F" \(" '{print $2}')

./out.py "$ips" "$macs" "$hosts"
