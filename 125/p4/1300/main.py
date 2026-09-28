# Perintah untuk mencetak tulisan ke dalam terminal (print statement):
# Sintaks -> print(<teks yang akan dicetak>)

# Contoh
# print("Hello world")  # cetak tulisan tanpa variabel

# message = "Hello world"
# print(message)  # cetak tulisan dengan variabel

# umur = 20
# print(umur)  # cetak angka

# Contoh string formatting
# Cara 1, menggunakan format f"{variabel}":
# nama = "Candra"
# print(f"Halo, {nama}")
# "Halo, {nama}"
# Untuk print kurung kurawal, gunakan kurung ganda (f"{{}}")

# Cara 2, menggunakan fungsi format()
# nama = "Budi"
# print("Halo, {}".format(nama))

# Cara 3, concatenation (penggabungan teks)
# prefix = "Hello, "
# nama = "Budi"
# print(prefix + nama)

# Algoritma (algorithm)
# is any well-defined computational procedure that takes
# some value, or set of values, as input and produces some value, or set of values, as
# output. (Cormen, 2009)

# An algorithm is said to be correct if, for every input instance, it halts with the
# correct output. We say that a correct algorithm solves the given computational
# problem.

# Contoh:
# Dari Manggarai jam 07.00, harus sampai kampus jam 07.20
# Input = Jam berangkat
# Prosedur = Cara untuk sampai ke kampus
# Output = Jam sampai kampus

# Input -> Proses -> Output

# Dalam python, kita bisa menggunakan fungsi input() untuk meminta masukan dari pengguna melalui terminal
# Sintaks: 
# <variabel> = input(<prompt>)

# nama = input("Masukkan nama Anda: ")
# print(f"Halo, {nama}")

# Fungsi input() menghasilkan variabel berbentuk teks/string
# umur = input("Masukkan umur Anda: ")  # Contoh: masukan 20
# umur_tahun_depan = umur + 1  # Error: beda variabel karena umur berbentuk teks, tidak bisa menjumlahkan nilai teks/str dengan angka
# print(f"Umur kamu tahun depan adalah {umur_tahun_depan}")  # Ekspektasi keluaran adalah: Umur kamu tahun depan adalah 21

# Solusinya, kita ubah tipe data "umur" ke dalam angka menggunakan fungsi int() atau float():
# umur = input("Masukkan umur Anda: ")  # tipe data string
# umur_int = int(umur)  # mengubah string menjadi integer
# umur_tahun_depan = umur_int + 1    # penjumlahan angka dengan angka
# print(f"Umur kamu tahun depan adalah {umur_tahun_depan}")  # Ekspektasi keluaran adalah: Umur kamu tahun depan adalah 21

# Fungsi
# Contoh fungsi yang sudah diterapkan
# 1. Print Statement (print())
# 2. Input Statement (input())
# 3. int()

# Fungsi custom / pendefinisian fungsi
# Sintaks:
# def <nama fungsi>(<argumen1>, <argumen2>, dst.):
#       <set of rules/proses/algoritma>
#       return <nilai yang diberikan/dikembalikan setelah fungsi dijalankan>

# Untuk menjalankan/memanggil fungsi:
# <variabel penyimpanan nilai hasil return> = <nama fungsi>(<argumen1>, <argumen2>, dst.)

# Contoh 1, membuat fungsi untuk menentukan umur di tahun depan:
def hitung_umur_tahun_depan(umur_tahun_ini):
    # Cara untuk menghitung umur berdasarkan variabel umur_tahun_ini
    umur_int = int(umur)  
    umur_tahun_depan = umur_int + 1    
    return umur_tahun_depan

# umur = input("Masukkan umur Anda: ")  # Input
# umur_tahun_depan = hitung_umur_tahun_depan(umur)  # Proses/set of rules
# print(f"Umur kamu tahun depan adalah {umur_tahun_depan}")  # Output

# Contoh 2, simulasi harga pembelian
def hitung_subtotal(harga_satuan, qty):
    # Butuh 2 argumen
    return int(harga_satuan)*int(qty)  #  rumus untuk menentukan harga total dari item

# Input
nama_barang = input('Masukkan nama barang: ')
harga_satuan = input('Masukkan harga: ')
jumlah_pembelian = input('Masukkan jumlah yang akan dibeli: ')

# Proses
subtotal = hitung_subtotal(harga_satuan, jumlah_pembelian)

# Output
print(f'Harga yang perlu kamu bayar adalah {subtotal}')

