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
    con = sqlite3.connect("database/credit_cards_" + str(size) + ".db")
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS accounts")
    cur.execute("CREATE TABLE accounts (first_name TEXT, last_name TEXT, card_number TEXT, cvv TEXT, expiry TEXT, address TEXT)")

    for i in range(size):
        while True:
            first_name = faker.first_name()
            last_name = faker.last_name()
            card_number = faker.credit_card_number()
            cvv = faker.credit_card_security_code()
            expiry = faker.credit_card_expire()
            address = faker.address()
            cur.execute("SELECT * FROM accounts WHERE card_number=?", (card_number,))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO accounts (first_name, last_name, card_number, cvv, expiry, address) VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, card_number, cvv, expiry, address))
                break
            else:
                continue


    con.commit()
    con.close()