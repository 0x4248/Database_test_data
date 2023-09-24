# Database test data
# A repository of databases for testing purposes
# https://www.github.com/lewisevans2007/Database_test_data
# By: Lewis Evans

import sqlite3
from faker import Faker

faker = Faker()

sizes = [100, 500, 1000, 5000, 10000]

for size in sizes:
    print("====================[ "+str(size)+" ]====================")
    con = sqlite3.connect("database/names_usernames_emails_passwords_" + str(size) + ".db")
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS accounts")
    cur.execute("CREATE TABLE accounts (first_name TEXT, last_name TEXT, username TEXT, email TEXT, password TEXT)")

    for i in range(size):
        while True:
            first_name = faker.first_name()
            last_name = faker.last_name()
            username = faker.user_name()
            email = faker.email()
            password = faker.password()
            cur.execute("SELECT * FROM accounts WHERE username=?", (username,))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO accounts (first_name, last_name, username, email, password) VALUES (?, ?, ?, ?)", (first_name, last_name, username, email, password))
                break
            else:
                continue


    con.commit()
    con.close()