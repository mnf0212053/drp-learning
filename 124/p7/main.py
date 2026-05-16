# Loop statement
# Berguna jika progam membutuhkan iterasi

# Memberikan notifikasi sebanyak 10x
# Gunakan "for" statement untuk meringkas program yang bersifat repetitif

import random

# basic
def for_loop1():
    for i in range(0, 10):
        print('Hello World!')

# nested for loop
def for_loop2():
    for i in range(0, 10):
        for j in range(0, 5):
            print(f'{i + 1}.{j}. Hello World!')

# iterasi tipe data list
list_kota = [
    {
        'id': 1,
        'kota': 'Bogor',
        'jumlah_kelurahan': 14
    },
    {
        'id': 2,
        'kota': 'Sukabumi',
        'jumlah_kelurahan': 20
    },
    {
        'id': 3,
        'kota': 'Purwakarta',
        'jumlah_kelurahan': 10
    },
]
print('Urutan perjalanan wisata:')

# membuat urutan perjalanan berdasarkan list kota yang disediakan
# hitung terlebih dahulu jumlah kota yang ada di dalam list
# cara 1: menggunakan indeks
def for_loop3():
    jumlah_kota = len(list_kota)

    for i in range(0, jumlah_kota):
        print(f'{i + 1}. {list_kota[i]["kota"]}')

# cara 2: iterasi variabel secara langsung
def for_loop4():
    n = 0
    for kota in list_kota:
        n = n + 1 # Increment
        print(f'{n}. {kota["kota"]} (jumlah kelurahan = {kota["jumlah_kelurahan"]})')

# fungsi ini menghasilkan list angka random
# cara 1: sediakan list kosong, kemudian ditambah menggunakan append
def generate_random1(count: int):
    nums = []

    for i in range(0, count):
        nums.append(random.randint(0,100))

    return nums

# cara 2: langsung diiterasikan pada return
def generate_random2(count: int):
    return [
        {
            'index': i,
            'value': random.randint(0, 100)
        }
        for i in range(0, count)
    ]

# while loop, lebih cocok untuk proses komputasi
def while_loop1():
    n = 0

    # ubah nilai n menjadi 7, namun lakukan dengan cara incremental
    while n < 7:
        n = n + 1
        print(n)

# continue untuk skip iterasi
def continue_func():
    n = 0
    for i in range(0,5):
        n = n + 1
        if i == 2:
            continue
        print(n)

# Iterasi tanpa henti
while True:
    print('Selamat datang di aplikasi X')
    print('1. Tampilkan data')
    print('2. Masukkan data')
    print('3. Analisis')
    print('4. Selesai')

    menu = input('Masukkan program yang akan dijalankan: ')
    if menu == '1':
        print('Data tampil')
        # isi source code sesuai dengan tujuan program/fitur
    elif menu == '2':
        data = input('Masukkan data: ')
        ###
    elif menu == '4':
        break # berfungsi untuk menghentikan iterasi

