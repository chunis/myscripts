#!/usr/bin/python

# Dennis Deng (ddeng@semtech.com)


import subprocess
import out
from bottle import route, run, template

nmap_cmd = 'sudo nmap -sP 192.168.1.1/24'
#own_ip_cmd = "ip addr show eth0 | grep -w inet | awk '{print $2}' | cut -d/ -f1"
own_ip_cmd = "ip addr show eno1 | grep -w inet | awk '{print $2}' | cut -d/ -f1"
#own_ip_cmd = "ifconfig eno1 | /bin/grep -w 'inet' | awk '{ print $2 }'"


def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output

def get_ip_mac_host():
    iplist = []
    maclist = []
    hostlist = []
    mhlist = []  # mac + host

    # find local ip
    own_ip = run_cmd(own_ip_cmd).strip()
    #print own_ip

    # get all IPs
    #output = subprocess.check_output(['sudo', 'nmap', '-sP', '192.168.1.1/24'])
    output = run_cmd(nmap_cmd)
    #print output
    #print '-----------'


    for line in output.split('\n'):
        if line.startswith('Nmap scan report'):
            iplist.append(line)
        elif line.startswith('MAC Address:'):
            mhlist.append(line)

    # clean ip list
    iplist = [x.split('for ')[1].strip() for x in iplist]
    iplist = [x for x in iplist if x != own_ip ]

    # get mac list and host list
    for x in mhlist:
        m, h = x.split(' (')
        maclist.append(m.split(': ')[1])
        hostlist.append(h[:-1])

    return (iplist, maclist, hostlist)

def output_txt():
    ips, macs, hosts = get_ip_mac_host()
    for i in range(len(ips)):
        print ips[i], '\t', macs[i], '\t', hosts[i]

def show_ip_in_html():
    ips, macs, hosts = get_ip_mac_host()
    return out.return_html(ips, macs, hosts)


if __name__ == '__main__':
    output_txt()
    #print show_ip_in_html()
