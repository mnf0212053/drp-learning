# Object Oriented Programming (OOP)
# Pemrograman Berorientasi Object
# Aplikasi penjualan rumah
# Buat program untuk entri data rumah
from houses.Houses import Houses


list_rumah = [] #  list objek rumah yang telah diinput

def hello(nama):
    print('Hello ' + nama)
    print('Apa kabar?')

def input_rumah():
    blok = input('Masukkan blok rumah: ')
    nomor = input('Masukkan nomor rumah: ')
    harga = input('Masukkan harga: ')
    rumah = Houses(blok, nomor, harga)

    list_rumah.append(rumah)

    print('Rumah berhasil diinput.\n')

def show_info_rumah():
    # buat notifikasi, jika tidak ada data rumah akan muncul notifikasi
    # "Data rumah belum tersedia."
    print('\nInfo rumah:')

    if len(list_rumah) == 0:
        print('===========================================')
        print('Data rumah belum tersedia.')
        print('===========================================\n')

    # terapkan looping dengan for untuk menampilkan info masing-masing rumah
    for rumah in list_rumah:
        rumah.info_rumah()

# buat fungsionalitasnya agar dapat mengakses menu dengan cara input angka
# 1. Input data
# 2. Cek info rumah

def navigasi():
    # Layer 2
    print('Selamat datang di aplikasi JualRumah.')
    print('1. Input data rumah')
    print('2. Cek info \n') #  \n = escape character untuk membuat baris baru
    
    pilihan = input('Masukkan menu: ')
    if pilihan == '1':
        input_rumah()
    elif pilihan == '2':
        show_info_rumah()


def main():
    # Layer 1
    navigasi()


if __name__ == '__main__':
    while True:
        # Ctrl + C untuk menghentikan program
        main()
    