#!/bin/python3

import socket,sys, getopt, threading
from datetime import datetime


ip = ''
ports = []

def banner():
	print ("-" * 50)
	print ("Please wait while we scan the target ports",str(ip))
	print ("-" * 50)

def help():
	print("For help use -h")
	print("Invalid argument.")
	print("Syntax: ./pexercise_02.py -i 192.168.0.123 -p 21,80")

def mainProcess():
	connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #This line will set the socket connection strings
	socket.setdefaulttimeout(0.1) 

	result = connect.connect_ex((rHost,int(port))) # 1 - Close & 0 - Open
	#print (result) - This will show the returns values from the connect attemped
	if result == 0:
		print ("Port {} is Open".format(port))
	else:
		print ("Port {} is Closed".format(port))
	
	connect.close()

try:
	options, args = getopt.getopt(sys.argv[1:], "hi:p:", ["help", "ip=", "port="])
except:
	help()
	sys.exit()
	
for option,val in options:
	if option in ('-h','--help'):
		print("Welcome to help menu \n -h : this comamand will guide you to help menu \n -i : ip address \n -ip : long form of -i \n -p : port to scan, can be a single port or many, ic case of many use comma \n -port : long form of -p")
	if option in ('-i','--ip'):
		ip = val
		print("ip", ip)
	if option in ('-p','--port'):
		if "," in val:
			ports = val.split(",")
			print("ports", ports)
		else:
			ports = val
			print("port", ports)


try:
	rHost = socket.gethostbyname(ip)
	if len(rHost) > 0:
		banner()
except:
	help()
	sys.exit()

time1 = datetime.now()

try:

	for port in ports:
		mainTread = threading.Thread(target=mainProcess)
		mainTread.start()
		mainTread.join()


	time2 = datetime.now()
	totaltime = time2 - time1

	print ("Port Scan Completed in: ", totaltime)

except KeyboardInterrupt:
	print ("\n Closing the program.")
	sys.exit()

except socket.gaierror:
	print ("\n Name or service Unknow.")
	sys.exit()
 
 
