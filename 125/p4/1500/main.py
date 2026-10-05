# Fungsi
# Digunakan untuk menyederhanakan program

# 1. Validasi
# 2. Komputasi
# 3. dst.

# Sintaks untuk mendefinisikan fungsi:
# def <nama fungsi>(<argumen1>, <argumen2>, dst.):
#      <algoritma/set of rules/langkah komputasi>
#       return <output fungsi>

# Untuk memanggil fungsi:
# <nama variabel untuk menyimpan output fungsi> = <nama fungsi>(<argumen1>, <argumen2>, dst.)
# Script yang terdapat di dalam fungsi tidak akan berjalan kecuali fungsi tersebut dipanggil

# Menggunakan def
def hitung_umur_tahun_depan(umur_saat_ini: str):
    # asumsikan umur_saat_ini berjenis string/teks, maka perlu diubah terlebih dahulu ke bentuk angka
    umur_saat_ini_int = int(umur_saat_ini)
    # kemudian lakukan komputasi untuk menentukan umur tahun depan
    umur_tahun_depan = umur_saat_ini_int + 1
    # gunakan return agar umur_tahun_depan dapat digunakan untuk proses yang lain
    return umur_tahun_depan

def hitung_umur_tahun_depan_ringkas(umur_saat_ini: str):
    return int(umur_saat_ini) + 1

# Menggunakan lambda
f = lambda x: int(x) + 1

# umur = input("Masukkan umur kamu: ")  # input
# umur_tahun_depan = hitung_umur_tahun_depan_ringkas(umur)  # proses
# print(f"Umur kamu adalah {umur}, tahun depan umur kamu adalah {umur_tahun_depan}")  # output

# Operator
# Jenis operator dalam Python:

# 1. Aritmatika
# 2. Assignment
# 3. Ternary
# 4. Comparison
# 5. Logical
# 6. Identitas
# 7. Membership
# 8. Bitwise

# 1. Aritmatika
# | +  | 	Addition	                x + y	
# | -  | 	Subtraction	                x - y	
# | *  | 	Multiplication	            x * y	
# | /  | 	Division	                x / y	
# | %  |    Modulus (sisa pembagian)    x % y	 
# | ** | 	Exponentiation	            x ** y	
# | // | 	Floor division	            x // y

# 2. Assigment
# =	    x = 5	x = 5	            Deklarasi Variabel
# +=	x += 3	x = x + 3           Increment  ->  variabel x harus dideklarasi terlebih dahulu
# -=	x -= 3	x = x - 3	        Decrement  ->  variabel x harus dideklarasi terlebih dahulu
# *=	x *= 3	x = x * 3	        Increment/Decrement 
# /=	x /= 3	x = x / 3	        Increment/Decrement
# %=	x %= 3	x = x % 3	        Increment/Decrement
# //=	x //= 3	x = x // 3	        Increment/Decrement
# **=	x **= 3	x = x ** 3	        Increment/Decrement
# &=	x &= 3	x = x & 3	        Increment/Decrement
# |=	x |= 3	x = x | 3	        Increment/Decrement
# ^=	x ^= 3	x = x ^ 3	        Increment/Decrement
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# :=	print(x := 3)	x = 3       Operator Walrus
# print(x)

# Contoh Increment/Decrement:
# x = 3  -> deklarasi terlebih dahulu
# x += 3   -> menambah nilai x sebesar 3

# Berlaku juga untuk string (penggabungan teks)
# mobil = "brio"
# mobil += "kijang"

# 3. Ternary
# Operator yang menghasilkan nilai bergantung kondisi
# Contoh, jika lulus maka nilai = 10, namun jika tidak maka nilai = 3:
# Sintaks:
# <variabel> = <nilai jika kondisi benar> if <kondisi> else <nilai jika kondisi salah>

# lulus = True
# nilai = 10 if lulus else 3

# 4. Comparison/Pembanding
# Untuk membandingkan satu nilai dengan nilai yang lain
# Menghasilkan nilai True/False dari operasi perbandingan tersebut

# ==	Equal	                    x == y	
# !=	Not equal	                x != y	
# >	    Greater than	            x > y	
# <	    Less than	                x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	    x <= y

# x = 3     Deklarasi Variabel
# x == 3    Membandingkan nilai x dengan angka 3

# Contoh penggunaan:
# x = 4
# y = 4
# is_equal = x == y  # True/False, bergantung apakah nilai x sama atau beda dengan y

# 5. Logical/Logika
# Membandingan nilai boolean satu dengan nilai boolean yang lain
# Hasil operator logika diperoleh dari tabel kebenaran
# and 	Returns True if both statements are true	                    x < 5 and  x < 10	
# or	Returns True if one of the statements is true	                x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not     (x < 5 and x < 10)

# Contoh konkrit
# is_graduated = True  # Flag kelulusan
# is_employed = False  # Flag pekerjaan
# graduated_and_employed = is_graduated and is_employed
# print(graduated_and_employed) 

# Note: Pada umumnya True bernilai 1 dan False bernilai 0 (mengikuti pola bilangan biner)

# 6. Identitas (berkaitan dengan objek)
# membandingkan objek, atau tipe data

# is 	    Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object

# 7. Membership
# Mengecek apakah nilai berada dalam suatu objek (list/dict)

# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# Contoh:
mobil = ['Avanza', 'Mobilio', 'Xenia']
# Cek apakah di dalam list "mobil" terdapat "Xenia"
is_xenia_exist = "Xenia" in mobil
print(is_xenia_exist)

# 8. Bitwise
# Membandingkan bilangan (biner)
# Sistem bilangan biner (3 digit):
# 0 = 000
# 1 = 001
# 2 = 010
# 3 = 011
# 4 = 100

# Bitwise menerjemahkan dua angka ke dalam bilangan biner, dan kemudian melakukan operasi logika terhadap masing-masing digitnya

# Contoh:
# 2 & 3
# Operasi:
# 010  -> biner dari 2
# 011  -> biner dari 3
# -----------------------  &
# 010  -> biner dari 2

# sehingga 2 & 3 = 2

# Contoh penerapan dalam settingan game
# digit 1: show hp bar
# digit 2: enable sound
  
# hp_bar = 1       -> 001
# enable_sound = 2 -> 010
# ------------------------ |
#                     011   -> 3

# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off