import sqlite3
import time

conn = sqlite3.connect('data.db')
cr = conn.cursor()

cr.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product VARCHAR,
        qty FLOAT,
        price_unit FLOAT,
        price_subtotal FLOAT
    )
""")

def get_total_price():
    cr = conn.cursor()
    cr.execute(
        """
        SELECT SUM(price_subtotal) FROM sales
    """
    )

    return cr.fetchone()[0]

if __name__ == '__main__':
    while True:
        print('Income = ' + str(get_total_price() or 0))
        time.sleep(1)
