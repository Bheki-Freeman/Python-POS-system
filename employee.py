import sqlite3
from getpass import getpass
con = sqlite3.connect('main.db')
cur = con.cursor()


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
        username = input('Enter username: ')
        userpass = getpass('Type Password: ')
        sql = "CREATE TABLE IF NOT EXISTS user(id integer primary key autoincrement not null, username, userpassword)"
        cur.execute(sql)
        data = [(None, username, userpass)]
        cur.executemany("INSERT INTO user VALUES(?, ?, ?)", data)
        con.commit()
        print('Registration Successful')

    def loginEmployee(self, user_name, userpass):
        sql = f"SELECT username, userpassword FROM user WHERE username='{user_name}' AND  userpassword='{userpass}'"
        cur.execute(sql)
        if not cur.fetchone():
            return False
        else:
            return True
