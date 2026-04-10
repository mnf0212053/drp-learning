# Readibility
from time import sleep  # ambil fungsi sleep dari modul time
# sleep berfungsi untuk pause program

# Ada 3 cara untuk melakukan looping
# 1. for (lebih sering digunakan, lebih aman karena kita menentukan sendiri iterasinya sampai berapa kali (jumlah iterasi))
#    penggunaan for ada 2 cara:
#    a. for i in range(awal, akhir)
#    b. for i in <iterable>
#       iterable = tipe data yang bisa diiterasikan
#       contoh: list ([1, 2, 3]), tuple ((1, 2, 3)), dict ({'umur': 20, 'sks': 24})
# 2. while (digunakan jika iterasi dilakukan berdasarkan suatu kondisi statement tertentu, misal, x > 10, dst., lebih berbahaya
#    karena jumlah iterasi ditentukan berdasarkan conditional statement)
# 3. rekursi (berbahaya, namun dalam suatu kondisi tertentu lebih praktis)

def loop1(jumlah_iterasi):
    # untuk penggunaan for i in range(awal, akhir)
    # ketika iterasi = jumlah_iterasi, maka iterasi selesai
    # iterasi dimulai ketika nilai iterasi = nilai_awal
    # jumlah_iterasi = 10
    nilai_awal = 0

    # fungsi range menghasilkan tipe data list 
    # yang isinya berupa list bilangan bulat 
    # dari nilai awal hingga nilai akhir secara berurutan
    for iterasi in range(nilai_awal, jumlah_iterasi):  
        print(iterasi)  # berjalan dari nilai_awal hingga jumlah_iterasi

def loop2():
    # untuk penggunaan for i in <iterable:list>
    nama_mahasiswa = [
        'andi', 
        'budi', 
        'clara', 
        'dedi', 
        'eko'
    ]

    # print masing-masing nama mahasiswa
    for nama in nama_mahasiswa:
        print(nama)

def loop3():
    # untuk penggunaan while, dengan jumlah iterasi yang tidak terdefinisi

    nilai = 0  # nilai awal

    # nilai_awal selalu bertambah satu untuk setiap iterasi
    # tambah kondisi looping, jika nilai > 10, maka iterasi berhenti
    # jarang digunakan karena logicnya berkebalikan
    # berbahaya karena dapat menyebabkan infinite looping
    # atau iterasi tak hingga
    while nilai <= 10: #  secara harfiah, selama nilai <= 10, iterasi akan berjalan
        print(nilai)
        nilai = nilai + 1  # diperlukan agar nilai bertambah (increment)
        sleep(1)  # pause 1 detik

def loop4():
    # selama nilai true, iterasi berjalan, dengan kata lain logic ini akan beriterasi terus menerus
    # sampai waktu yang tidak ditentukan (sampai python berhenti)
    # gunakan ctrl + c untuk terminasi paksa jika terkena infinite looping
    # gunakan break untuk menghentikan looping
    # jika tetap tidak bekerja, harus dilakukan proses kill
    # pastikan kursor terfokus di terminal, bukan di lembar kerja
    
    # misal, akan dilakukan looping sebanyak 10 kali ==> berhenti jika n > 10

    n = 0  # nilai awal
    while True:  
        print("tes 123")
        sleep(0.2)
        
        # gunakan if statement untuk mengkondisikan syarat agar berhenti
        if n > 10:
            break

        n = n + 1 #  increment

def loop5(nilai):
    # untuk rekursi: memanggil fungsi yang sama di dalam fungsi tersebut
    # berguna untuk fungsi faktorial
    
    # nilai! = (nilai - 1)*(nilai - 2)* ... *1 
    if nilai == 0:
        return loop5(nilai)
    
    return nilai*loop5(nilai-1)

