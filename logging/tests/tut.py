import requests

data_file = open("tests/tut-file.txt")
data = data_file.readlines()
data_file.close()

url = data[0]
successful_login_url = data[1]

login_cookies = eval(data[2])

with requests.Session() as session:
    response_url = session.post(url, data=login_cookies).url

if response_url != url:
    print("tut.py - ✔")

else:
    print("tut.py - ✖")