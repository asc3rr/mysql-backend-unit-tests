test_name = input("[?] Enter test name -> ")

mysql_login_data_input = input("Enter mysql login data (view README file) -> ").split("_")

mysql_login_data = {}

for data_cell in mysql_login_data_input:
    data = data_cell.split(":")
    mysql_login_data.update({data[0]:data[1]})

table_name = input("Enter table name that should change after request -> ")

login_site_url = input("Enter login site url -> ")
successful_login_site_url = input("Enter url of site that should appear after logging in -> ")

login_data_input = input("Enter login data (view README file) -> ").split("_")

login_data = {}

for data_cell in login_data_input:
    data = data_cell.split(":")
    login_data.update({data[0]:data[1]})

after_login_site_url = input("Enter url of site -> ") #wysyłamy tam dane
after_login_cookies_input = input("Enter data that should be sent to the site (view README file) -> ").split("_")

after_login_cookies = {}

for data_cell in after_login_cookies_input:
    data = data_cell.split(":")
    after_login_cookies.update({data[0]:data[1]})

#creating files
data_file_content = f"{mysql_login_data}\n{table_name}\n{login_site_url}\n{successful_login_site_url}\n{login_data}\n{after_login_site_url}\n{after_login_cookies}"

file_content = """import requests
import MySQLdb

#Getting data from file
data_file = open("tests/%s-file.txt")
data = data_file.readlines()
data_file.close()

mysql_login_data = eval(data[0])
table_name_that_should_update = data[1]

#logging into website
login_site_url = data[2]
successful_login_url = data[3]
login_data = eval(data[4])

#data to post after login
after_login_url = data[5]
after_login_cookies = eval(data[6])

#Getting number of rows before query
db = MySQLdb.connect(host=mysql_login_data["login"], user=mysql_login_data["user"], passwd=mysql_login_data["password"], db=mysql_login_data["db_name"])

cursor = db.cursor()

cursor.execute(f"SELECT * FROM {table_name_that_should_update}")

num_rows_before_request = cursor.rowcount

#Making request
with requests.Session() as session:
    response_url = session.post(login_site_url, data=login_data).url #logging in

    #comparing urls
    if response_url == successful_login_url:
        session.post(after_login_url, data=after_login_cookies) #posting data

        cursor.execute(f"SELECT * FROM {table_name_that_should_update}")

        num_rows_after_request = cursor.rowcount

        #comparing rows number
        if num_rows_after_request > num_rows_before_request:
            print("%s.py - ✅")

        else:
            print("%s.py - ❌")

    else:
        print("%s.py - ❌")""" % (test_name, test_name, test_name, test_name)

data_file = open(f"tests/{test_name}-file.txt", "w")
data_file.write(data_file_content)
data_file.close()

test_file = open(f"tests/{test_name}.py", "w")
test_file.write(file_content)
test_file.close()