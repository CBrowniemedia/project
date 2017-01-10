#03-07-2013
#inserting data into an existing table

import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name,Price) values(?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    product = ("Espresso",1.5)
    product = ("Latte",1.35)
    product = ("Mocha", 2.40)
    product = ("Green tea",1.20)
    product = ("Black tea",1.00)
    product = ("Americano",1.50)
    for each in product:
        insert_data(product)
