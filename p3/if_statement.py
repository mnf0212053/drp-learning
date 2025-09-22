x = 5


def if_statement_1():
    masukan = input('Masukkan suatu nilai: ')

    # misalkan, dibutuhkan suatu logic bahwa
    # 1. Jika masukan bernilai lebih dari 10, maka akan muncul
    #    notifikasi "Nilai ini lebih besar dari 10!"
    # 2. Jika masukan bernilai lebih kecil dari 10, maka akan
    #    muncul notifikasi "Nilai ini terlalu kecil!"
    # 3. Jika masukan bernilai sama dengan 10, maka akan muncul
    #    notifikasi "Nilainya cocok!"

    if int(masukan) > 10:  #  12 > 10 v    5 < 10  x
        print('Nilai ini lebih besar dari 10!')  # sintaks: print("wording")
    elif int(masukan) < 10:  #  5 < 10  v
        print("Nilai ini terlalu kecil!")  # Tanda kutip menandakan tipe data string
    elif int(masukan) == 11:
        # lakukan sesuatu
        # tidak berjalan karena sudah cocok dengan masukan > 10
        # (logic pertama)
        print("Fungsi ini tidak berjalan")  
    else:
        print("Nilainya cocok!")

def if_statement_2():
    masukan = input('Masukkan suatu nilai: ')
    masukan_int = int(masukan)

    nilai_tambahan = x  # tidak perlu import kembali modul if_statement.x jika bekerja di dalam file/modul if_statement.py

    nilai_akhir = masukan_int + nilai_tambahan  # perhitungan nilai akhir
    
    if nilai_akhir > 10:  #  12 > 10 v    5 < 10  x
        print('Nilai ini lebih besar dari 10!')  # sintaks: print("wording")
    elif nilai_akhir < 10:  #  5 < 10  v
        print("Nilai ini terlalu kecil!")
    else:
        print("Nilainya cocok!")

# definisi fungsi
def perkenalan():
    print('hallo, perkenalkan nama saya budi')

# eksekusinya
if __name__ == '__main__':
    print('hello world')