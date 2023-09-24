# Database test data
# A repository of databases for testing purposes
# https://www.github.com/lewisevans2007/Database_test_data
# By: Lewis Evans

import sqlite3
from faker import Faker
import hashlib

faker = Faker()

sizes = [100, 500, 1000, 5000, 10000]

for size in sizes:
    print("====================[ "+str(size)+" ]====================")
    con = sqlite3.connect("database/usernames_passwords_hashed" + str(size) + ".db")
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS accounts")
    cur.execute("CREATE TABLE accounts (username TEXT, sha256 TEXT, md5 TEXT)")

    for i in range(size):
        while True:
            username = faker.user_name()
            password = faker.password()
            cur.execute("SELECT * FROM accounts WHERE username=?", (username,))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO accounts (username, sha256, md5) VALUES (?, ?, ?)", (username, hashlib.sha256(password.encode()).hexdigest(), hashlib.md5(password.encode()).hexdigest()))
                break
            else:
                continue


    con.commit()
    con.close()