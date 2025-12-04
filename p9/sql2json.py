import sqlite3
import json

conn = sqlite3.connect('data.db')

def convert():
    cr = conn.cursor()
    cr.execute(
        """
            SELECT * FROM sales
        """
    )

    sales = cr.fetchall()
    data = []

    for sale in sales:
        data.append(
            {
                'id': sale[0],
                'product': sale[1],
                'qty': sale[2],
                'price_unit': sale[3],
                'price_subtotal': sale[4],
            }
        )

    # Create JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # Create JSONL file
    with open('data.jsonl', 'w') as f:
        for d in data:
            json.dump(d, f)
            f.write('\n')

if __name__ == '__main__':
    convert()
    print('Data berhasil diimport')