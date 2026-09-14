# Ini adalah file python dengan nama file main.py
# main = nama file
# .py = ekstensi untuk python
# Contoh ekstensi
# .pdf -> buka dokumen
# .doc / .docx -> file document
# .xls / xlsx -> file excel
# .ppt / .pptx -> file powerpoint
# Ekstensi selalu diawali dengan titik (.) tanpa ada titik tambahan di belakangnya
# myfile.docx.xlsx -> file .xlsx

# struktur penamaan file <nama file><ekstensinya>

# Tanda Hastag mengindikasikan komentar (tidak akan dijalankan oleh Python)

# variabel = simbol yang menandakan suatu nilai yang bisa berubah
# contoh: x = 4
# x -> variabel
# 3 -> nilai
# penamaan variabel berfungsi untuk memperjelas konteks
# Contoh:
# 1. tempat_lahir = "Bogor"  V
# 2. domisili = "Bogor"   V
# kedua variabel beda konteks, meskipun nilainya sama
# 3. x = "Bogor" 
# variabel ketiga memiliki konteks yang kurang jelas, sehingga maknanya ambigu
# jika ada spasi, umumnya diganti dengan underscore (_)
# contoh: tempat lahir -> tempat_lahir

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

# Sequence Types:	list, tuple, range (array)
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
