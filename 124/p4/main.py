print('Inisiasi program')

def add():  # Fungsi penjumlahan
    # Perintah yang tertulis di dalam fungsi tidak akan dijalankan jika tidak dipanggil
    print("Melakukan penjumlahan")
    # Deklarasi variabel
    a = 3
    b = 4

    # Komputasi
    # Variabel c ini hanya bisa diakses di dalam fungsi ini (variabel lokal)
    c = a + b

    # Mengembalikan suatu nilai
    # return ini hanya dapat digunakan di dalam fungsi
    # tanpa return, fungsi akan mengembalikan None
    return c

def f():
    print('Mengembalikan angka 1') #  Perintah ini tidak berada di dalam fungsi apapun
    return 1

k = f()
l = add()
print(k)