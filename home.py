# This is the home page(Where all the mechanism takes place)
from datetime import date, datetime
import sqlite3
import logging
from products import Product
import sys
from employee import Employee

today = date.today()
curr_time = datetime.now()
line = '^'*60
real_time = f'{curr_time.hour}:{curr_time.minute}:{curr_time.second}'
con = sqlite3.connect('main.db')
cur = con.cursor()
product = Product()
employee = Employee()


def start():
    print(f'\n{line}\n\t[DATE]: {today} \t [TIME]: {real_time}\n{line}')
    print('\nWELCOME: Choose what to do below: \n\t1 --- New Sale\n\t2 --- Products\n\t3 --- Employees\n\t0 --- Logout ->: ')
    choice = int(input('Choice: '))
    if choice == 1:
        makeSale()
    elif choice == 2:
        prodFunction()
    elif choice == 3:
        emp_choice = int(input(f'{line}\n\t[WELCOME ADMINISTRATOR] \n{line}\nChoose what to do below,\
              \n1 --- Display Eployees\n2 --- Find employee\n3 --- Update Employee\n4 --- Delete Employee\n5 --- Home\n$--> '))
        if emp_choice == 1:
            employee.displayAllEmployees()
        elif emp_choice == 2:
            employee.findEmployee()
        elif emp_choice == 3:
            # employee.updateEmployee()
            pass
        elif emp_choice == 4:
            # employee.removeEmployee()
            pass
        elif emp_choice == 5:
            start()
        else:
            print('[ERROR]: Wrong user input! (choose from 1 - 5)')
    elif choice == 0:
        pass
    else:
        print('[WRONG INPUT!]')


def prodFunction():
    print(f'\n\t[AVAILABLE PRODUCTS]\n{line}\n')
    product.retriveProducts()
    print(f'{line}\n1 --- Add New Products\n2 --- Update an Item\n3 --- Find an Item\n4 --- Remove Product\n5 --- Home\n')
    product_choice = int(input("$--> "))
    if product_choice == 1:
        product.createProduct()
    elif product_choice == 2:
        product.updateProductDetails()
    elif product_choice == 3:
        product.getProduct()
    elif product_choice == 4:
        product.deleteProduct()
    elif product_choice == 5:
        start()
    else:
        print('Wrong input!')


def makeSale():
    bought_items = []
    skucode = 0
    print('New Transaction: ')
    # Selling details: sku_code (from cashier), from db: proname, price, desc, quant
    while skucode != -1:
        try:
            # Use this skucode to fetch the item from db
            skucode = int(input('Enter Sku Code or -1 to [CONTINUE]: '))
            if skucode == -1:
                break
            sql = f'SELECT * FROM products WHERE skucode={skucode}'
            if not cur.execute(sql).fetchone():
                print('[ERROR]: skucode not found!')
                continue
            for row in cur.execute(sql).fetchall():
                skucode, prodname, price, desc, quantity = row
                bought_item = f'{skucode} {prodname} E{price} {desc} {quantity}'
                bought_items.append(bought_item)
        except ValueError as ve:
            print(ve)
    print(f'{line}\n\tPurchase list \n{line}')  # Kind of reciept
    for item in bought_items:
        print('\t%s' % (item))
    print(f'{line}')
    nextCustomer()


def nextCustomer():
    next_cust = input('Next Customer? [Yes or No]: ')
    try:
        if next_cust.lower() == 'yes':
            start()
        else:
            sys.exit(0)
    except ValueError:
        logging.error('[INPUT ERROR!]: Please type in \'yes\' or \'no\'!')


# Run this module in case of debuging!
# if __name__ == '__main__':
#     start()
