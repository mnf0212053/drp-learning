from manager.search import search_products
from manager.output import print_products

def display_menu():
    # Tampilan pilihan menu (UI)
    print('================================')
    print('Selamat datang di toko ATK')
    print('1. Cari Barang')
    print('2. List Keranjang')
    print('3. Pengaturan profil')
    print('4. Selesai')  # Fitur untuk menghentikan program
    print('================================')

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
    elif menu == '3':
        # Logic untuk fitur pengaturan profil
        print('Anda mengakses menu "Pengaturan profil"')
    elif menu == '4':
        # Logic untuk keluar program
        print('Keluar program') # Notifikasi agar program lebih user-friendly
        return True #  memberikan nilai True jika no 4 dipilih (menyelesaikan program)
    else:
        # Logic jika inputan tidak sesuai dengan yang ada di pilihan
        print('Menu tidak ada')
    return False