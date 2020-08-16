test_name = input("[?] Enter test name -> ")

file_content = """import requests

data_file = open("tests/%s-file.txt")
data = data_file.readlines()
data_file.close()

url = data[0]
successful_login_url = data[1]

login_cookies = eval(data[2])

with requests.Session() as session:
    response_url = session.post(url, data=login_cookies).url

if response_url != url:
    print("%s.py - ✅")

else:
    print("%s.py - ❌")""" % (test_name, test_name, test_name)

url = input("Enter logging site url -> ")
successful_login_url = input("Enter url of site that should appear after succesful login -> ")

login_cookies_input = input("Enter login cookies (e.g. 'login':'asc3rr'_'password':'123456') -> ").split("_")

login_cookies = {}

for cookie in login_cookies_input:
    data = cookie.split(":")
    login_cookies.update({data[0]:data[1]})

data_file_content = f"{url}\n{successful_login_url}\n{login_cookies}"

test_file = open(f"tests/{test_name}.py", "w")
test_file.write(file_content)
test_file.close()

data_file = open(f"tests/{test_name}-file.txt", "w")
data_file.write(data_file_content)
data_file.close()