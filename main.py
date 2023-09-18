''' 
    In this program, I will be demonstrating a login program(console) using the sqlite
    database, We'll take the user name and password for now, since I have been learning sqlite today

'''
from getpass import getpass
from datetime import date, datetime
from home import start as start_h
from employee import Employee

today = date.today()
now = datetime.now()
line = '^'*60
emp = Employee()


def start():
    choice = 0
    print(
        f'\t[DATE]: {today} [TIME]: {now.hour}:{now.minute}:{now.second}\n{line}')
    try:
        choice = int(input(
            '\n\tChoose what to do below:\n[1 --- Register]\n[2 --- Login]\n[0 --- Exit] :-> '))
        if choice == 1:
            emp.registerEmployee()
        elif choice == 2:
            print(f'{line}\n\tLogin here: ')
            nam = input('Enter your username: ')
            passw = getpass('Type Password: ')
            if not emp.loginEmployee(nam, passw):
                print(f'[ERROR!]: Caught Wrong Credentials!\n')
                start()
            start_h()
        elif choice == 0:
            exit(0)
        else:
            print('[WRONG INPUT!]')
    except ValueError as ve:
        print("[INVALID LITERALS]:Please type in Digits!")


if __name__ == '__main__':
    start()
