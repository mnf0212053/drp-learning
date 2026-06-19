from sqlite3 import connect, Connection

from action import get_user_id, login, product_list, product_detail, buy, register, sales_list
from typing import Callable


APP_TITLE = 'SHOPY: Belanja Murah dan Cepat:'
LIST_MENU: list[tuple[int, str, Callable[..., None]]] = [
    (1, 'Lihat Detail Produk', product_detail),
    (2, 'Beli Produk', buy),
    (3, 'List produk yang sudah dibeli', sales_list)
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

def portal(conn: Connection):
    while True:
        print(APP_TITLE)
        print('1. Login')
        print('2. Register')
        act = input('Pilih aksi: ')

        if act == '1':
            login(conn)
        elif act == '2':
            register(conn)
            continue

        if get_user_id():
            return

if __name__ == '__main__':
    conn = db_connect()
    portal(conn)

    while True:
        display_menu(conn)
        select_menu(conn)
