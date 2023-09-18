''' 
    In this file, I will be demonstrating a login program(console) using the sqlite
    database, We'll take the user name and password for now, since I have been learning sqlite today

'''
import sqlite3
from datetime import date, datetime
from home import start as start_h
from getpass import getpass
import logging

con = sqlite3.connect("main.db")
cur = con.cursor()
today = date.today()
now = datetime.now()
line = '^'*60


def registerUser():  # my simple registration algorithm
    print('Welcome to our simple registration')
    username = input('Enter username: ')
    userpass = getpass('Type Password: ')
    sql = "CREATE TABLE IF NOT EXISTS user(id integer primary key autoincrement not null, username, userpassword)"
    cur.execute(sql)
    data = [(None, username, userpass)]
    cur.executemany("INSERT INTO user VALUES(?, ?, ?)", data)
    con.commit()
    print('Registration Successful')


def loginUser(user_name, userpass):  # Simple login algorithm
    sql = f"SELECT username, userpassword FROM user WHERE username='{user_name}' AND  userpassword='{userpass}'"
    cur.execute(sql)
    if not cur.fetchone():
        return False
    else:
        return True


def start():
    choice = 0
    print(
        f'\t[DATE]: {today} [TIME]: {now.hour}:{now.minute}:{now.second}\n{line}')
    try:
        choice = int(input(
            '\n\tChoose what to do below:\n[1 --- Register]\n[2 --- Login]\n[0 --- Exit] :-> '))
        if choice == 1:
            registerUser()
        elif choice == 2:
            print(f'{line}\n\tLogin here: ')
            nam = input('Enter your username: ')
            passw = getpass('Type Password: ')
            if not loginUser(nam, passw):
                print(f'[ERROR!]: Caught Wrong Credentials!\n')
                start()
            start_h()
        elif choice == 0:
            exit(0)
        else:
            print('[WRONG INPUT!]')
    except ValueError as ve:
        print("[INVALID LITERALS]:Please type in Digits!")

if __name__=='__main__':
    start()

cur.close()
con.close()
