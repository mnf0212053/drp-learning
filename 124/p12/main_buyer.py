from sqlite3 import connect, Connection

from action import product_list, product_detail, buy
from typing import Callable


APP_TITLE = 'SHOPY: Belanja Murah dan Cepat:'
LIST_MENU: list[tuple[int, str, Callable[..., None]]] = [
    (1, 'Lihat Detail Produk', product_detail),
    (2, 'Beli Produk', buy)
]

def db_connect() -> Connection:
    return connect('shopydb.db')

def display_menu(conn: Connection):
    print('=============================================')
    print(APP_TITLE)
    print('=============================================')
    print('=============================================')
    product_list(conn)
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

    while True:
        display_menu(conn)
        select_menu(conn)
