#!/usr/bin/python
#
# About: Find the IP address of an Linux server by ssh account
# Chunis Deng (chunchengfh@gmail.com)
#

import pxssh
from multiprocessing import Process
from getpass import getpass

range_start = 1
range_end = 255


def check_sftp(host, u, p):
	s = pxssh.pxssh()
	try:
		if not s.login (host, u, p):
			#print "SSH session failed on login:", host
			pass
		else:
			print "SSH session login successful:", host, 'as', u
			#s.sendline ('ls -l')
			#s.prompt()         # match the prompt
			#print s.before     # print everything before the prompt.
			s.logout()
	except:
		pass


if __name__ == '__main__':
	user = raw_input("ssh username: ")
	passwd = getpass("ssh password: ")
	ip_head = raw_input("ip section (xx.xx.xx, such as '192.168.1'): ")
	ip_list = ip_head.split('.')
	if len(ip_list) < 3:
		print "ip section error!"
		import sys
		sys.exit()

	for x in range(range_start, range_end):
		ip = '.'.join(ip_list[:3] + [str(x)])
		p = Process(target=check_sftp, args=(ip, user, passwd))
		#print "Add %d" %x
		p.start()
		#p.join()
