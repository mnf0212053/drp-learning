import sqlite3
import time
import json
import random

conn = sqlite3.connect('data.db')

def buy():
    # buka file master data terlebih dahulu
    with open('product.json') as f:
        products = json.load(f)

    # product
    index = random.randint(0, len(products) - 1)
    product = products[index]['product']

    # qty
    qty = random.randint(1, 10)
    
    # price_unit
    price_unit = products[index]['price_unit']

    cr = conn.cursor()
    cr.execute(
        """
            INSERT INTO sales (product, qty, price_unit, price_subtotal)
            VALUES (?, ?, ?, ?)
        """
    , (product, qty, price_unit, qty*price_unit))

    print('Pembelian + ' + product + ' dengan jumlah ' + str(qty))

    conn.commit()


if __name__ == '__main__':
    while True:
        buy()
        time.sleep(0.1)
