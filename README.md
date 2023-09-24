# Database test data

A repository of databases for testing purposes

## Databases

The databases are stored at `database/` directory. The data is under the table `accounts`. There are 5 different sizes of databases: 100, 500, 1000, 5000, 10000.

The following databases are available:

- credit_cards_xxx.db (first_name, last_name, credit_card_number, cvv, expiration_date, address)
- names_usernames_passwords_xxx.db (first_name, last_name, username, password)
- names_usernames_emails_passwords_xxx.db (first_name, last_name, username, email, password)
- usernames_passwords_xxx.db (username, password)
- usernames_passwords_hashed_xxx.db (username, sha256, md5)

## License

The data is free to use for any purpose. The data is provided "as is" without any warranty of any kind, either express or implied without limitation any implied warranties of merchantability or fitness for a particular purpose. In no event shall the author or copyright holder be liable for any damages whatsoever.