import sqlite3
from getpass import getpass
from datetime import date

con = sqlite3.connect('main.db')
cur = con.cursor()
line = '^'*60



class Employee():
    # empcode, empname, gender, phone, jobtitle, department, datejoined
    def setValues(self, emp_code, emp_name, gender, phone, job_title, department, datejoined):
        self.empcode = emp_code
        self.empname = emp_name
        self.gender = gender
        self.phone = phone
        self.jobtitle = job_title
        self.department = department
        self.datejoined = datejoined

    def registerEmployee(self):
        print('Welcome to our simple registration')
        empcode = input('Enter Emp Code [BF100]: ')
        empname = input('Enter username: ')
        gender = input('Enter Gender: ')
        job = input('Enter job title: ')
        phone = int(input('Enter Phone number [26876294516]: '))
        deprt = input('Enter department: ')
        datejoined = date.today()
        emppass = getpass('Type Password: ')
        self.setValues(empcode, empname, gender, phone, job, deprt, datejoined)
        sql = "CREATE TABLE IF NOT EXISTS users(\
            empcode text primary key,\
            empname,\
            gender,\
            phone int,\
            jobtitle text,\
            department text,\
            datejoined date,\
            userpassword)"
        cur.execute(sql)
        data = [(self.empcode, self.empname, self.gender, self.phone, self.jobtitle,\
                self.department, self.datejoined, emppass)]
        cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
        con.commit()
        print('Registration Successfull')

    def loginEmployee(self, user_name, userpass):
        sql = f"SELECT empname, userpassword FROM users WHERE empname='{user_name}' AND  userpassword='{userpass}'"
        cur.execute(sql)
        if not cur.fetchone():
            return False
        else:
            return True

    def displayAllEmployees(self):
        try:
            sql = 'SELECT empcode, empname, gender, phone, jobtitle, department, datejoined FROM users'
            print(f'\n\t[AVAILABLE EMPLOYEES]\n{line}')         
            for row in cur.execute(sql).fetchall():
                empcode, empname, gender, phone, jobtitle, department, datejoined = row
                print('{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}'.format(empcode, empname, gender,\
                        phone, jobtitle, department, datejoined))
        except ValueError as ve:
            print(ve)
    def findEmployee(self):
        try:
            empcode = input('Enter employee Code to search: ')
            sql = f"SELECT * FROM users WHERE empcode='{empcode}'"
            result = cur.execute(sql).fetchall()
            if not result:
                print('[ERROR]:Employee Code NOT Found!')
            else:
                for row in result:
                    empcode, empname, gender, phone, jobtitle, department, datejoined, userpassword = row
                    print('{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}'.format(empcode, empname, gender,\
                            phone, jobtitle, department, datejoined, userpassword))
        except ValueError as ve:
            print(ve)

