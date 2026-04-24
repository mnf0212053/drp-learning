# Tipe data
# 1. Angka
#    a. Integer (bilangan bulat (contoh: 1, 2, 3, dst.))
#       i. Short -> 2 byte => hanya bisa deklarasi variabel maksimal 16 bit (1111111111111111) => 2^16 - 1 = 65535 (bukan fitur python)
#       ii. Long -> 4 byte => 2^32 - 1  (bukan fitur python)
#    b. Float (bilangan dengan koma (contoh: 1.1, 2.7, 3.14))
# 2. Teks/string
# 3. Boolean
# 4. Array/List => mengandung banyak nilai
# 5. Tuple
# 6. Dictionary

# Bilangan desimal: bilangan basis 10 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Bilangan biner: bilangan basis 2

# 00 -> 2 bit

# 0 = 000  -> 3 bit
# 1 = 001
# 2 = 010
# 3 = 011
# 4 = 100
# dst ...

# 11111111  -> 8 bit = 1 byte


# Number
x = 3  # integer
y = 3.14  # float
c = 3.80  # float
z = 4.00  # float
a = float(x)  # mengubah string/integer menjadi float  
b = int(c)  # (1) mengubah string/float ke integer  (2) pembulatan ke bawah (misal, 3.80 -> 3)

# String
m = "Hello World"
no_telepon = "081234567890"
message = 'Halo semua!'
text1 = "i don't have cookie"
text2 = 'They said "eat the cookie!"'
text3 = """They said \"i don't know\\\\ about it.\""""

# Boolean (hanya ada dua nilai: True atau False)
sudah_makan = False
is_connected = True

# List
a = [1, 2, 3]  # list hanya angka
student = [1, "John Smith"]  # list gabungan angka dan string
employee = ["Thom Haye", "Netherlands"]  # list hanya string
b = [[1, 2, 3], [4, 5, 6]]  # list dalam list
c = [
    1,
    6,
    8
]  # list dengan format vertikal (tujuan hanya estetika agar mudah dibaca)

# Tuple (versi immutable dari list)
t = (1, 2, 3) 

# Dictionary (key-value pairs). key dalam bentuk string
mahasiswa = {
    'nim': "1244163312",
    'nama': "Budi",
    'umur': 20,
    'nilai': {
        'data_raya': 'B',
        'basis_data': 'A'
    },
    'mata_kuliah': [
        'Aljabar Linear',
        'Pemrograman Web'
    ]
}

# =====================================================================================
# Input statement
# Meminta masukan melalui konsol (masukan diterima dalam bentuk string)

nama = input("Masukkan nama kamu: ")
umur = input("Masukkan umur kamu: ")  
# Jika angka hendak dilakukan operasi matematika, maka harus diubah 
# kedalam bentuk angka terlebih dahulu menggunakan int() atau float()

# cara 1
print('Halo', nama)

# cara 2
print(f'Halo {nama}!')

# cara 3
print('Halo {}!'.format(nama))

# cara 4
print('Halo %s!!' % nama)

# gabungkan nama dengan umurnya 5 tahun mendatang
print('Halo %s! Umur kamu 5 tahun mendatang adalah %s' % (nama, int(umur) + 5))
