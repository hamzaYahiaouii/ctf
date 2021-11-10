

import requests
import hashlib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

targeturl = "http://165.22.121.146:31554/"



s = requests
res1 = s.get(targeturl)
print("get request cookie is: ", res1.cookies)
soup = BeautifulSoup(res1.text,'lxml')

for heading in soup.find_all(["h3"]):
	hashh = heading.text.strip()

print(hashh)

result = hashlib.md5(hashh.encode("utf-8")).hexdigest()
print(result)
param = {"hash":result}

res2 = s.post(targeturl,data=param, cookies=res1.cookies)

print("get responce cookie is: ", res1.cookies)
print(res2.text)

