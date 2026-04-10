# fungsi

# fungsi tanpa argumen
def hello1():
    print('hello 1')

def hello2():
    print('hello 2')

# fungsi dengan argumen
# sintaks: def nama_fungsi(argumen1, argumen2, dst.)
# argumen bisa lebih dari satu
def panggil_nama(nama, umur): # argumennya adalah nama dan umur, harus ada argumen saat fungsi ini dipanggil
    print('hello ' + nama)
    print('umur kamu ' + str(umur) + ' tahun')
    x = input('apa kabar? ')
    if x == 'baik':
        print('alhamdulillah')
    else:
        print('semoga membaik')

# fungsi yang memberikan nilai (ada return statement)
# 1. Return digunakan untuk terminasi logic
# 2. Bisa digunakan untuk berbagai tipe data, jika tidak ada argumen, 
#    maka dia akan return None
# 3. Nilai yang diberikan atau direturn bisa lebih dari satu
def penjumlahan(a, b):
    # fungsi ini memberikan suatu nilai jika dipanggil 
    # (dalam kasus ini, fungsi ini memberikan nilai penjumlahan antara a dan b)
    nilai_akhir = a + b
    return nilai_akhir, "ini adalah fungsi penjumlahan dimana " + str(a) + " + " + str(b) + " = " + str(a+b)

def pengurangan(a, b):
    return a - b