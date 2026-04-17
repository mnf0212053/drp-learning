def add_tanpa_argumen():  # Fungsi penjumlahan
    # Perintah yang tertulis di dalam fungsi tidak akan dijalankan jika tidak dipanggil
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

def add_dengan_argumen(angka1, angka2): # Ambil dua nilai dari argumen untuk dijumlahkan
    hasil = angka1 + angka2
    return hasil  # ekivalen dengan return angka1 + angka2

def f():
    print('Mengembalikan angka 1') #  Perintah ini tidak berada di dalam fungsi apapun
    return 1