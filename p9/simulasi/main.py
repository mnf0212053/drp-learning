import sqlite3
import json
import random
import time

conn = sqlite3.connect('..\\data.db')

cr = conn.cursor()

def insert(product: str, qty: float, price_unit: float):
    cr = conn.cursor()
    cr.execute("""
        INSERT INTO sales (product, qty, price_unit, price_subtotal) VALUES (?, ?, ?, ?)
    """, (product, qty, price_unit, qty*price_unit))
    conn.commit()

def simulate():
    # load master product
    with open('product.json', 'r') as f:
        products = json.load(f)
    
    # pick product from rng
    index = random.randint(0, len(products) - 1)
    product = products[index]

    # pick random qty
    qty = random.randint(1, 10)

    # logging
    print("Order for {} (Unit Price {}) with quantity {}".format(product['product'], product['price_unit'], qty))

    # insert to db
    insert(product['product'], qty,product['price_unit'])

if __name__ == '__main__':
    while True:
        simulate()
        time.sleep(1)
