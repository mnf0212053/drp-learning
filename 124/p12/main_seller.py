from sqlite3 import connect, Connection

from action import product_list_seller, product_create, sales_list, sales_list_by_product
from typing import Callable

APP_TITLE = 'SHOPY Seller: Membantu Bisnis Anda Berkembang'
LIST_MENU: list[tuple[int, str, Callable[..., None]]] = [
    (1, 'List Produk', product_list_seller),
    (2, 'Buat Produk', product_create),
    (3, 'Lihat Data Penjualan', sales_list),
    (4, 'Data Penjualan Per Produk', sales_list_by_product)
]
DB_TABLES = [
    """        
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            code VARCHAR(255) NOT NULL UNIQUE,
            description TEXT,
            price_unit FLOAT NOT NULL
        );
    """,
    """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            price_total FLOAT,
            FOREIGN KEY (product_id)
            REFERENCES products(product_id)
        )
    """
]

def db_connect() -> Connection:
    return connect('shopydb.db')

def init(conn: Connection):
    for query in DB_TABLES:
        conn.execute(query)
    print('Database Initialized.')

    return

def display_menu(conn: Connection):
    print('=============================================')
    print(APP_TITLE)
    print('=============================================')
    print('Menu')

    for menu in LIST_MENU:
        print(f'{menu[0]}. {menu[1]}')

def select_menu(conn: Connection):
    menu = int(input('Masukkan menu: '))

    # Gunakan filter untuk mengambil elemen tertentu dari list
    selected_menu = list(filter(lambda m: m[0] == menu, LIST_MENU))

    # Validasi jika menu tidak ada (jika menu tidak tersedia, selected_menu = [])
    if not selected_menu:
        print('Menu tidak tersedia')

    # Eksekusi menu
    selected_menu[0][2](conn)

if __name__ == '__main__':
    conn = db_connect()
    init(conn)

    while True:
        display_menu(conn)
        select_menu(conn)
