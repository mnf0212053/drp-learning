from sqlite3 import connect, Connection

from action import export_sales, product_list_seller, product_create, sales_list, sales_list_by_product, users_list
from typing import Callable

APP_TITLE = 'SHOPY Seller: Membantu Bisnis Anda Berkembang'
LIST_MENU: list[tuple[int, str, Callable[..., None]]] = [
    (1, 'List Produk', product_list_seller),
    (2, 'Buat Produk', product_create),
    (3, 'Lihat Data Penjualan', sales_list),
    (4, 'Data Penjualan Per Produk', sales_list_by_product),
    (5, 'Export Data Penjualan', export_sales),
    (6, 'List User', users_list)
]
DB_TABLES: list[str] = [
    """
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            sale_id INTEGER NOT NULL,
            review TEXT,
            rating INTEGER NOT NULL,
            FOREIGN KEY (product_id)
            REFERENCES products(product_id)
            FOREIGN KEY (user_id)
            REFERENCES users(user_id)
            FOREIGN KEY (sale_id)
            REFERENCES sales(sale_id)
        )
    """,
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
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """,
    """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            price_total FLOAT,
            user_id INTEGER,
            FOREIGN KEY (product_id)
            REFERENCES products(product_id)
            FOREIGN KEY (user_id)
            REFERENCES users(user_id)
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
