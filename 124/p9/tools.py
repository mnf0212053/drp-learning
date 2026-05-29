from manager.search import search_products
from manager.output import print_products

import json

def select_menu(menu):
    # Seleksi menu
    if menu == '1':
        # Logic untuk fitur pencarian barang
        print('Anda mengakses menu "Cari Barang"')

        query = input('Masukkan query: ')
        products = search_products(query)
        print_products(products)
    elif menu == '2':
        # Logic untuk fitur list keranjang
        print('Anda mengakses menu "List Keranjang"')
        with open('keranjang.json', 'r') as f:
            data = json.load(f)
            f.close()

        for i in data:
            print(i)
    elif menu == '3':
        # Logic untuk fitur pengaturan profil
        print('Anda mengakses menu "Pengaturan profil"')
    elif menu == '4':
        # input
        with open('keranjang.json', 'r') as f:
            list_produk = json.load(f)
            f.close()

        produk = input('Masukkan produk')

        # simpan data
        # 1. file storage
        # 2. sql
        list_produk.append(produk)

        with open('keranjang.json', 'w') as f:
            json.dump(list_produk, f, indent=2)
            f.close()

    elif menu == '99':
        # Logic untuk keluar program
        print('Keluar program') # Notifikasi agar program lebih user-friendly
        return True #  memberikan nilai True jika no 4 dipilih (menyelesaikan program)
    else:
        # Logic jika inputan tidak sesuai dengan yang ada di pilihan
        print('Menu tidak ada')
    return False