# Operator
# Jenis operator dalam Python:

# 1. Aritmatika
# 2. Assignment
# 3. Ternary
# 4. Comparison
# 5. Logical
# 6. Identitas - skip
# 7. Membership
# 8. Bitwise - skip

# ==========================================
# 1. Aritmatika
# Operasi manipulasi matematika 
# | +  | 	Addition	                x + y	
# | -  | 	Subtraction	                x - y	
# | *  | 	Multiplication	            x * y	
# | /  | 	Division	                x / y	
# | %  |    Modulus (sisa pembagian)    x % y	 
# | ** | 	Exponentiation	            x ** y	
# | // | 	Floor division	            x // y

# Contoh addition:
# x = 2 + 3  # -> Hasil 5 (x = 5)
# Contoh subtraction:
# x = 2 + 3  # -> Hasil -1 (x = -1)
# Contoh modulus (sisa pembagian):x = 1 % 2
# Contoh 2 % 3
#    0.6
#   ___________________________
# 3 | 20
#     18
#   ------------------------------ -
#      2  -> modulus

# Contoh 1 % 2
#   0.5
#  _______________________________
# 2| 10
#  | 10
#  ----------------------------- -
#     0

# Contoh Floor Division (membagi, kemudian melakukan pembuatan ke bawah)
# x = 5 // 3  # -> hasil bagi = 1.67, lalu dibulatkan ke bawah (floor)

# Contoh penjumlahan dalam string:
# nama = "Budi"
# pesan = "Halo"
# hasil = nama + pesan  # -> Concatenation (memadukan satu teks dengan teks yang lain)
# print(hasil)

# 2. Assigment
# =	    x = 5	x = 5	            Deklarasi Variabel
# +=	x += 3	x = x + 3           Increment  ->  variabel x harus dideklarasi terlebih dahulu
# -=	x -= 3	x = x - 3	        Decrement  ->  variabel x harus dideklarasi terlebih dahulu
# *=	x *= 3	x = x * 3	        Increment/Decrement 
# /=	x /= 3	x = x / 3	        Increment/Decrement
# %=	x %= 3	x = x % 3	        Increment/Decrement
# //=	x //= 3	x = x // 3	        Increment/Decrement
# **=	x **= 3	x = x ** 3	        Increment/Decrement

# Contoh assignment dengan +=
# x = 3  # -> Deklarasi variabel x dengan nilai sebesar 3
# x = x + 3  # -> Menambahkan nilai x sebesar 3  -> increment  -> x = 6
# x += 3 # -> cara singkat increment nilai x sebesar 3  -> x = 9
# print(x)  # berapa hasil 

# Contoh assignment dengan -=
# x = 10  # -> Deklarasi variabel x dengan nilai sebesar 3  x = 10
# x = x - 3  # -> Menambahkan nilai x sebesar 3  -> increment  -> x = 7
# x -= 5 # -> cara singkat increment nilai x sebesar 3  -> x = 2

# 3. Ternary
# Operator yang menghasilkan nilai bergantung kondisi
# Sintaks:
# <variabel> = <nilai jika kondisi True> if <kondisi (True/False) else <nilai jika kondisi False>

# Contoh:
# is_passed = False
# grade = 100 if is_passed else 40
# print(grade)

# 4. Comparison/Pembanding
# Untuk membandingkan satu nilai dengan nilai yang lain
# Menghasilkan nilai True/False dari operasi perbandingan tersebut

# ==	Equal	                    x == y	
# !=	Not equal	                x != y	
# >	    Greater than	            x > y	
# <	    Less than	                x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	    x <= y

# Bedakan: 
# x = 3     Deklarasi Variabel (assignment)
# x == 3    Menentukan apakah nilai x sama dengan dengan angka 3

# Contoh penggunaan x == y:
# x = 4
# y = 4
# is_equal = x == y  # True/False, bergantung apakah nilai x sama dengan y
# print(is_equal)

# Contoh penggunaan x != y:
# x = 4
# y = 4
# is_equal = x != y  # True/False, bergantung apakah nilai x berbeda dengan y
# print(is_equal)

# 5. Logical/Logika
# Membandingan nilai boolean satu dengan nilai boolean yang lain
# Hasil operator logika diperoleh dari tabel kebenaran
# and 	Returns True if both statements are true	                    x < 5 and  x < 10	
# or	Returns True if one of the statements is true	                x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not     (x < 5 and x < 10)

# x = True and False
# print(x)

# Contoh konkrit
# is_graduated = True  # Flag kelulusan
# is_employed = False  # Flag pekerjaan
# # definsikan variabel is_fresh_graduate (fresh graduate) 
# # yang ciri-cirinya adalah sudah lulus *dan* belum bekerja
# is_fresh_graduate = is_graduated and is_employed
# print(is_fresh_graduate) 

# Note: Pada umumnya True bernilai 1 dan False bernilai 0 (mengikuti pola bilangan biner)

# 7. Membership
# Mengecek apakah nilai berada dalam suatu objek (list/dict)

# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# Contoh:
mobil = ['Avanza', 'Mobilio', 'Xenia']
# Cek apakah di dalam list "mobil" terdapat "Xenia"
is_xenia_exist = "Xenia" in mobil
print(is_xenia_exist)