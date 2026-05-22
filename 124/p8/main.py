# Penyimpanan data

# Komponen aplikasi perangkat lunak:
# 1. Create (membuat)
# 2. Read (membaca)
# 3. Update (mengubah/edit)
# 4. Delete (menghapus)

# Contoh: Aplikasi e-commerce (sisi customer)

# Import module (dependensi):
# ada 2 cara:
# 1. import <nama_modul>
# 2. from <nama_modul> import <nama_fungsi>

# Contoh module: numpy, matplotlib, random, sqlite3, json

from tools import display_menu, select_menu

# __name__ nama file python

if __name__ == '__main__': #  mencegah source code dijalankan dari fungsi import
    while True: #  Endless loop (gunakan Ctrl + C di console untuk menghentikan program)
        display_menu()

        # Request masukan dari user terhadap menu yang akan diakses
        menu = input('Masukkan menu yang dipilih: ')

        is_done = select_menu(menu=menu)  # parameter yang menyatakan bahwa program sudah selesai
        if is_done:  # Jika program sudah selesai
            break

