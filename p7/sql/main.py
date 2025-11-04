# Hierarki SQL:
# 1. Database
# 2. Tabel
# 3. Field
# 3. Data / Record

# Cara akses SQL:
# 1. Query (seperti yang sudah dicontohkan)
# 2. ORM (Object Relational Mapper) -> diluar scope


import sqlite3

conn = sqlite3.connect('mydb.db')

cr = conn.cursor()
cr.execute(
    """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            nama TEXT,
            umur INTEGER
        )
    """
)

def _load_data():
    query = """
        SELECT id, nama, umur FROM users
    """

    cr = conn.cursor()
    cr.execute(query)
    data = cr.fetchall()
    return data

def load_data():
    data = _load_data()
    print(data)

def save_data():
    nama = input('masukkan nama: ')
    umur = input('masukkan umur: ')

    # Query ini rawan terkena serangan SQL Injection
    # query = """
    #     INSERT INTO users (nama, umur) VALUES (""" + nama + """, """ + umur + """)
    # """
    
    # Query aman, menggunakan prepared statement
    query = """
        INSERT INTO users (nama, umur) VALUES (?, ?)
    """

    cr = conn.cursor()
    cr.execute(query, (nama, umur))
    conn.commit()

def delete_data():
    id = input('masukkan id yang akan dihapus: ')

    query = """
        DELETE FROM users WHERE id=?
    """

    cr = conn.cursor()
    cr.execute(query, (id,))
    conn.commit()

if __name__ == '__main__':
    while True:
        print('Menu:')
        print('1. Load Data')
        print('2. Save Data')
        print('3. Delete Data')
        menu = input('menu: ')

        if menu == '1':
            load_data()
        elif menu == '2':
            save_data()
        elif menu == '3':
            delete_data()