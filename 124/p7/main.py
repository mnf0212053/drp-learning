# Loop statement
# Berguna jika progam membutuhkan iterasi

# Memberikan notifikasi sebanyak 10x
# Gunakan "for" statement untuk meringkas program yang bersifat repetitif

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
n = 0
for kota in list_kota:
    n = n + 1 # Increment
    print(f'{n}. {kota["kota"]} (jumlah kelurahan = {kota["jumlah_kelurahan"]})')
