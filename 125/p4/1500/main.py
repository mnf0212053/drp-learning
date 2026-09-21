# ========================================================================================================================
# Program Hello World
# Print statement -> pernyataan untuk mencetak suatu teks ke dalam terminal
# Berfungsi untuk menampilkan keluaran (output) dari program
# Sintaks: print(<teks yang akan dicetak/tampil>)

# Contoh 1:
# Print statement tanpa variabel
# print("Hello Worlds") 

# Contoh 2:
# Print statement dengan variabel
# message = "Ini adalah teks yang ditampung di dalam variabel 'message'"
# print(message)    

# Contoh 3:
# Print statement dengan string formatting
# nama = "Budi"  # Deklarasi Variabel "nama"
# cuaca = "cerah"

# Cara 1, menggunakan prefiks "f" di depan string:
# print(f"Halo {nama}, cuacanya {cuaca} ya!")

# Cara 2, menggunakan fungsi format:
# print("Halo {}, cuacanya {} ya!".format(nama, cuaca))

# ========================================================================================================================
# Running program Python:

# Input Statement
# Berfungsi untuk meminta masukan (input) dari pengguna melalui CLI/Terminal
# Sintaks:
# <variabel> = input(<prompt>)
# Contoh 1:

# nama = input("Masukkan nama: ")  # Input
# print(f"Halo, {nama}!")

# fungsi input perlu ditampung dalam suatu variabel agar dapat diolah. 
# tipe data dari variabel tersebut berbentuk teks/string.

# Contoh 2:
umur = input("Masukkan umur kamu: ")
# umur_tahun_depan = umur + 1  # -> baris ini error karena menjumlahkan string dan angka, harus disamakan terlebih dahulu
umur_tahun_depan = int(umur) + 1  # -> fungsi int() digunakan untuk mengubah string menjadi integer
print(f"Umur kamu adalah {umur}, tahun depan umur kamu adalah {umur_tahun_depan}")

# Fungsi
# contoh: f(x) = x + 1  -> fungsi dalam matematika
# format fungsi dalam programming -> <nama fungsi>(<argumen1>, <argumen2>, <dst>)
# identik dengan f(x, y) = 2xy + y^2

# Cara 1 melalui CLI (full)
# 1. Melalui CLI, navigasi ke direktori yang memiliki file python yang akan dirunning (menggunakan perintah "cd" dalam terminal)
# 2. Jalankan perintah "python <nama file python>" -> contoh: python main.py

# Cara 2 (menggunakan absolute path)
# 1. Di dalam explorer, pilih file yang akan dirun (misal, main.py di dalam folder 1500). Klik kanan pada file tersebut.
# 2. Pilih "Copy Path"
# 3. Di terminal, ketik "python " (dengan spasi), kemudian paste path tersebut menggunakan ctrl + v atau klik kanan pada mouse/touchpad
# Contoh:
# python C:\Users\mnurf\Documents\Projects\work\drp\125\p4\1500\main.py  -> run perintah ini untuk menjalankan file python tersebut

# Tip: Jangan lupa mengaktifkan auto-save agar perubahan dalam file langsung tersimpan (File -> Centang Auto-save)
