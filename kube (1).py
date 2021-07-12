#!/usr/bin/python3

import cgi		
import subprocess
import time

print("content-type: text/html")
print()

#filestorage to take the input
f = cgi.FieldStorage()
cmd = f.getvalue("x")



#use sudo to run docker perfectly
o=subprocess.getoutput("sudo " + cmd)
print(o)
