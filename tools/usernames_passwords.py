# Database test data
# A repository of databases for testing purposes
# https://www.github.com/0x4248/Database_test_data
# By: 0x4248

import sqlite3
from faker import Faker

faker = Faker()

sizes = [100, 500, 1000, 5000, 10000]

for size in sizes:
    print("====================[ "+str(size)+" ]====================")
    con = sqlite3.connect("database/usernames_passwords_" + str(size) + ".db")
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS accounts")
    cur.execute("CREATE TABLE accounts (username TEXT, password TEXT)")

    for i in range(size):
        while True:
            username = faker.user_name()
            password = faker.password()
            cur.execute("SELECT * FROM accounts WHERE username=?", (username,))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, password))
                break
            else:
                continue


    con.commit()
    con.close()