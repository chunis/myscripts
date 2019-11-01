#!/usr/bin/python

# Dennis Deng (ddeng@semtech.com)

import sys

head = '''
<html>
    <head>
        <style>
            table, th, td {
              border: 1px solid black;
              border-collapse: collapse;
            }
            th, td {
              padding: 10px;
            }
        </style>
    </head>
    <body>
        <table>
        <tr>
            <th>IP</th>
            <th>MAC</th>
            <th>Host</th>
        </tr>
'''
foot = '''
        </table>
    </body>
</html>
'''

def output_html(iplist, maclist, hostlist):
    print head
    for i in range(len(iplist)):
        print '<tr>',
        #print iplist[i], '\t', maclist[i], '\t', hostlist[i]
        print '<td>%s</td><td>%s</td><td>%s</td>' %(iplist[i], maclist[i], hostlist[i]),
        print '</tr>'
    print foot

def return_html(iplist, maclist, hostlist):
    ret = []
    ret.append(head)
    for i in range(len(iplist)):
        tmp = '<td>%s</td><td>%s</td><td>%s</td>' %(iplist[i], maclist[i], hostlist[i])
        ret.append('<tr>')
        ret.append(tmp)
        ret.append('</tr>')
    ret.append(foot)
    return '\n'.join(ret)

if __name__ == '__main__':
    ips = sys.argv[1].split('\n')
    macs = sys.argv[2].split('\n')
    hosts = sys.argv[3].split('\n')
    output_html(ips, macs, hosts)
