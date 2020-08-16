import requests
import MySQLdb

#Getting data from file
data_file = open("tests/TEST-NAME-file.txt")
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
            print("TEST-NAME.py - ✅")

        else:
            print("TEST-NAME.py - ❌")

    else:
        print("TEST-NAME.py - ❌")