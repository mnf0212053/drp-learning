# Ini adalah file python dengan nama file main.py
# main = nama file
# .py = ekstensi untuk python
# Contoh ekstensi
# .pdf -> buka dokumen
# .doc / .docx -> file ms. word
# .xls / xlsx -> file excel
# .ppt / .pptx -> file powerpoint
# Ekstensi selalu diawali dengan titik (.) tanpa ada titik tambahan di belakangnya
# myfile.docx.xlsx -> file .xlsx

# struktur penamaan file <nama file><ekstensinya>

# Tanda Hastag mengindikasikan komentar (tidak akan dijalankan oleh Python)

# variabel = simbol yang menandakan suatu nilai yang bisa berubah
# contoh 1: x = 4
# x -> variabel
# 4 -> nilai
# contoh 2: x = 5
# variabel x tetap sama
# nilainya berbeda

# dalam Python, Untuk kasus nilai x dideklarasikan dua kali:
# x = 3
# x = 5
# Python akan menggunakan nilai x terakhir

# penamaan variabel berfungsi untuk memperjelas konteks
# Contoh:
# 1. tempat_lahir = "Bogor"  V
# 2. domisili = "Bogor"   V
# kedua variabel beda konteks, meskipun nilainya sama
# 3. x = "Bogor" 
# variabel ketiga memiliki konteks yang kurang jelas, sehingga maknanya ambigu
# jika ada spasi, umumnya diganti dengan underscore (_)
# contoh: tempat lahir -> tempat_lahir
# variabel diawali dengan alfabet, bukan dengan angka
# 3_pendidikan_terakhir X
# tiga_pendidikan_terakhir V
# tempat-lahir X -> dianggap sebagai pengurangan

# TIPE DATA
# Text Type:	str (teks/string)
# Umumnya digunakan untuk tulisan, tidak dapat dioperasikan secara matematis ( + - , dst.)
# indikator tipe data string adalah tanda petik ' atau ""
# Contoh:
nama = 'Budi'  # X
domisili = "Bandung"

# Untuk tipe string dapat menggunakan petik (") sebanyak tiga rangkap untuk teks yang
# panjang dan membutuhkan baris baru
# Contoh:
about_me = """Saya adalah seorang mahasiswa.
    Setiap hari saya pergi ke kampus."""

# Numeric Types:	int, float, complex (angka)
# Tipe data angka, umumnya dipakai untuk nilai yang bisa dikalkulasikan secara aritmatika
# Jenis tipe data angka:
# 1. int (integer/bilangan bulat (1, 2, 3, dst.))
#    1.1 -> bukan bilangan bulat
# Contoh:
umur = 20

# bedakan dengan berikut
# umur = '20'  # variabel ini berjenis teks/string

# 2. float (bilangan koma)
# Contoh:
tebal_buku = 3.5

# 3. kompleks (bilangan imajiner/akar -1)
# fasa = 3*i + 5
# i = bilangan imajiner atau akar -1

# Contoh operasi aritmatika
# 1. penjumlahan
estimasi_lulus = umur + 2

# 2. pengurangan
tahun_masuk = umur - 2

# 3. perkalian
x = 2*3

# 4. pembagian
x = 3/2

# Boolean Type:	bool
# hanya memiliki dua nilai (true/false)
# Contoh 1: apakah user sudah terkonfirmasi
is_confirmed = True

# Sequence Types:	list, tuple (array)
# Tipe data yang nilainya lebih dari satu, paling sering digunakan dalam pengolahan data

# 1. List []
# Contoh: Mengukur tinggi badan mahasiswa
tinggi_badan = [170, 163, 165, 160]

# 2. Tuple ()
subtotal = (5000, 20000)

# Mapping Type:	dict (objek)
# objek yang memiliki berbagai variabel, dinyatakan dengan tanda {}
# umumnya disebut sebagai pasangan key-value. 
# Key (kunci) umumnya digunakan sebagai konteks dari value/nilai
# Key umumnya ditulis dalam teks/string, namun bisa juga dalam angka
# Contoh 1:
user_profile = {
    'name': "Budi Santoso",
    'username': 'budi123',
    'umur': 20,
    'is_verified': True,
    'nilai_ujian': [
        70,
        80,
        85,
        95
    ]
}

# Contoh 2 (array dari objek)
user_profiles = [
    {
        'name': "Budi Santoso",
        'username': 'budi123',
        'umur': 20,
        'is_verified': True,
        'nilai_ujian': [
            70,
            80,
            85,
            95
        ]
    },
    {
        'name': "Abdul Manaf",
        'username': 'abdul2000',
        'umur': 25,
        'is_verified': False,
        'nilai_ujian': [
            80,
            70,
            75,
            80
        ]
    }
]

# Contoh 2: apakah user sudah registrasi
is_registered = False

# Binary Types:	bytes, bytearray, memoryview
# tipe biner, umumnya digunakan untuk file (gambar, video, pdf, dst.)

# None Type:	NoneType
# tipe kosong, tidak memiliki nilai. 
# Umumnya digunakan untuk placeholder atau deklarasi 
# bisa juga menandakan variabel tersebut belum diisi
# Contoh: user belum memasukkan domisili
domisili = None
