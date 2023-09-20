import sqlite3


con = sqlite3.connect('main.db')
cur = con.cursor()
line = '^'*60

class Product():
    #  sku_code (from cashier), from db: proname, price, desc, quant
    def setProductDetails(self, skucode, prodname, price, desc, quantity):
        self.skucode = skucode
        self.prodname = prodname
        self.price = price 
        self.desc = desc
        self.quantity = quantity

    def createProduct(self):
        print(f'{line}\n\t[CREATING A NEW PRODUCT]\n{line}\n')
        try:
            self.skucode = int(input('Enter skucode: '))
            self.prodname = input('Enter product name: ')
            self.price = float(input('Enter Price: '))
            self.desc =  input('Type in some product description: ')
            self.quantity = int(input('Enter total quantity: '))
            self.insertIntoDb()
        except ValueError:
            print('[ERROR]: Input Mismatch!!')

    def insertIntoDb(self):
        data = [(self.skucode, self.prodname, self.price, self.desc, self.quantity)]
        sql = "INSERT INTO products (skucode, prodname, price, desc, quantity) values(?, ?, ?, ?, ?)"
        cur.executemany(sql, data)
        con.commit()    
        print(f'New Item Saved successfully!')    
    
    def retriveProducts(self):
        sql = "SELECT * FROM products"
        result = cur.execute(sql).fetchall()
        for row in result:
            skucode, prodname, price, desc, quantity = row
            print(f'{skucode:6}  {prodname:20}  {price:5}  {desc:30}  {quantity:4}') #better formatting

    def getProduct(self):
        sku = int(input('Enter skucode to find: '))
        sql = f"SELECT * FROM products WHERE skucode='{sku}'"
        result = cur.execute(sql).fetchone()
        if result:            
            skucode, prodname, price, desc, quantity = result
            print('{:<5} {:<10} {:<5} {:<20} {:<5}'.format(skucode, prodname, price, desc, quantity))
        else:
            print('Skucode not Found!')


    def updateProductDetails(self):
        prod_code = int(input('Enter the product sku code to update: '))
        new_code = int(input('Enter new skucode: '))
        new_name = input('Enter New name: ')
        new_price = float(input('Enter new price: '))
        new_desc = input('Enter new Description: ')
        new_quantity = int(input('Enter new quantity : '))
        sql = f"UPDATE products SET skucode='{new_code}', prodname='{new_name}', price='{new_price}', desc='{new_desc}',\
             quantity='{new_quantity}' WHERE skucode='{prod_code}'"
        if cur.execute(sql):
            con.commit()
            print(f'Product Details Updated!')
        else:
            print('%s'%'Failed to update Details!')
    def deleteProduct(self):
        sku = int(input('Enter Skucode to delete: '))
        sql = f"DELETE FROM products WHERE skucode='{sku}'"
        if cur.execute(sql):
            con.commit()
            print('Product Removed!')
        else:
            print('Failed to Remove Product!')
