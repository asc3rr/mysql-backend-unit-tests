import mysql.connector as conn
import requests
import json

def login(login_url, successful_login_url, login_data):
    with requests.Session() as session:
        response = session.post(login_url, data=login_data)

        if response.url == successful_login_url:
            return True, session

        else:
            return False, session

def send_data(url, data, session=False):
    if not session:
        requests.post(url, data=data)

        return None

    else:
        session.post(url, data=data)

        return session

def get_num_rows(mysql_data:dict):
    host = mysql_data["host"]
    user = mysql_data["user"]
    password = mysql_data["password"]
    db_name = mysql_data["db_name"]
    table = mysql_data["table_name"]

    num_rows = 0

    db = conn.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    cursor = db.cursor()

    cursor.execute(f"SELECT * FROM {table}")

    result = cursor.fetchall()

    for i in result:
        num_rows += 1

    return num_rows


settings = json.load(open("settings.json"))

login_url = settings["login_url"]
successful_login_url = settings["after_login_url"]
login_data = settings["login_data"]

main_url = settings["main_url"]
main_data = settings["main_data"]

mysql_data = settings["mysql_data"]

is_login_test = settings["is_login_test"]
is_using_session = settings["is_using_session"]

is_success, session = login(login_url, successful_login_url, login_data)

if is_login_test:
    is_success, session = login(login_url, successful_login_url, login_data)

    if is_success:
        print("Success")

    else:
        print("Failed")

    exit()

else:
    if is_using_session:
        is_success, session = login(login_url, successful_login_url, login_data)

        if not is_success:
            print("Login failed")

        else:
            num_rows_before_request = get_num_rows(mysql_data)

            send_data(main_url, main_data, session=session)

            num_rows_after_request = get_num_rows(mysql_data)

            if num_rows_before_request != num_rows_after_request:
                print("Success")

            else:
                print("Failed")

    else:
        num_rows_before_request = get_num_rows(mysql_data)

        send_data(main_url, main_data)

        num_rows_after_request = get_num_rows(mysql_data)

        if num_rows_before_request != num_rows_after_request:
            print("Success")

        else:
            print("Failed")