import sqlite3
        
def insert_data(product):
        sql = "insert into Product(Name, Price) values (?,?)"
        cursor.execute(sql,product)
        db.commit()

if __name__ == "__main__":

    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
    counter = 1
    while counter == 1:
        product = []
        drink = input("Please input a drink.")
        price = input("Please input it's price.")
        product = [drink, price]
        insert_data(product)
        yn = input("Do you want to add another drink? (y/n)")
        if yn == "y":
            counter = 1
        else:
            counter = 2
    

