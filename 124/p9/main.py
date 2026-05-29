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

from display.menu import display_menu
from tools import select_menu
import sqlite3 #  tidak ada form, semua dependensi/fungsi diimport

# __name__ nama file python

if __name__ == '__main__': #  mencegah source code dijalankan dari fungsi import
    # Inisiasi/create basis data
    connection = sqlite3.connect('mydb.db')

    # Create table
    # 1. Tabel keranjang

    # Contoh create table
    # CREATE TABLE Persons (
    #     PersonID int PRIMARY KEY,  -> unique identifier
    #     LastName varchar(255) NOT NULL,
    #     FirstName varchar(255),
    #     Address varchar(255),
    #     City varchar(255)
    # );  IF NOT EXISTS untuk mencegah error karena tabel sudah ada
    connection.execute(
        """
            CREATE TABLE IF NOT EXISTS keranjang (
                id int PRIMARY KEY,
                nama_barang varchar(255),
                qty int
            );
        """
    )  # Menjalankan file sql

    # Program/sistem utama
    while True: #  Endless loop (gunakan Ctrl + C di console untuk menghentikan program)
        display_menu()

        # Request masukan dari user terhadap menu yang akan diakses
        menu = input('Masukkan menu yang dipilih: ')

        is_done = select_menu(menu=menu)  # parameter yang menyatakan bahwa program sudah selesai
        if is_done:  # Jika program sudah selesai
            break

