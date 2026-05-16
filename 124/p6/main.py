# IF STATEMENT

# - Menggunakan sintaks "if"
# - Sintaks (if <boolean>)
# - Di dalam alur if harus terdapat indentasi secara koding

def check_tujuan(terdesak=False):
    # nilai default terdesak = False
    if terdesak:
        # perintah di dalam ini hanya akan berfungsi hanya jika nilai terdesak = True
        tujuan = 'kampus'
    else:
        # perintah di dalam ini hanya akan berfungsi hanya jika nilai terdesak = False
        tujuan = 'stasiun'

    return tujuan

# Alternatif penulisan if statement
# menggunakan nilai default
# praktek yang lebih baik, karena lebih efisien

def check_tujuan2(terdesak):
    tujuan = 'stasiun'  # nilai default dari tujuan

    if terdesak:
        # perintah di dalam ini hanya akan berfungsi hanya jika nilai terdesak = True
        tujuan = 'kampus'

    # OUT
    return tujuan

# setelah if tidak harus secara gamblang mengevaluasikan langsung true-false
# if False:
#     print('Apakah tulisan ini muncul?')
# alternatifnya, kita bisa menggunakan operator logika

# Tabel kebenaran
# - AND
#     A  |   B    |   OUTPUT
# ----------------------------
#     v  |   v    |     v
#     v  |   x    |     x
#     x  |   v    |     x
#     x  |   x    |     x

# - OR
#     A  |   B    |   OUTPUT
# ----------------------------
#     v  |   v    |     v
#     v  |   x    |     v
#     x  |   v    |     v
#     x  |   x    |     x

# - NOT (penegasian, not A)
#     A    |   OUTPUT
# ----------------------------
#     v    |     x
#     x    |     v

# misal:
# 1. Hujan dan berangin
# 2. Hujan atau berangin

# OPERASI AND (A and B)
# 1. Jika hujan dan berangin, maka saya tetap di rumah
# 2. Hari ini hujan dan tidak berangin
# 3. Saya tidak tetap di rumah (stay = False)

# OPERASI OR (A or B)
# 1. Jika hujan atau berangin, maka saya tetap di rumah
# 2. Hari ini hujan dan tidak berangin
# 3. Saya tetap di rumah (stay = True)

def is_stay(hujan, berangin):
    if hujan and berangin: # Jika hujan dan berangin
        stay = True # saya tetap di rumah
    else:
        stay = False

    return stay

# OUTPUT
if is_stay(True, False):
    print('saya tetap di rumah')
else:
    print('saya keluar rumah')
