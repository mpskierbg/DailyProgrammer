import sqlite3
import os.path

sqlite_file = input("what is your file name? ") + '.sqlite'# name of the sqlite database file
table_name = input('enter name of the table? ')  # name of the table to be created

if not os.path.isfile(sqlite_file):
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    print("Opened database successfully")
    conn.execute('''CREATE TABLE {tn}
         (NAME          TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         USERNAME        CHAR(50))'''\
         .format(tn=table_name))
    print("Table created successfully")

name = input("What is your first and last name? > ")
age = input("How old are you? > ")
username = input("What is your reddit username? > ")

print("your name is " + name + ", you are " + age + " years old, and your reddit username is " + username)

conn = sqlite3.connect(sqlite_file)
conn.execute("insert into {tn} (NAME, AGE, USERNAME) values (?, ?, ?)"\
        .format(tn=table_name),
        (name, age, username))

print("Database updated")

conn.commit()
conn.close()
