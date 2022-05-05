#!/usr/bin/env python3

#importing neccessory file
import os 
import sys

def ftp(p='21'):
	os.system("python -m pyftpdlib -p " + f"{p}" + " --write")

if len(sys.argv) ==2 :
	port_number = sys.argv[-1]
	ftp(port_number)

else:
	ftp()