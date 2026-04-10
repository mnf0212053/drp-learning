import if_statement as ifs  # memanggil / menjalankan semua fungsi yang ada menggunakan alias (as).
from konstanta import nilai_pi, nilai_e  # hanya memanggil nilai_pi dan nilai_e

# Note: pastikan nama alias bukan nama yang sudah digunakan oleh python, seperti print, input, if, is, dll. Bisa dilihat dari warna font.

# Looping Statement
# For
# While

if __name__ == '__main__':
    # Tipe data
    text = "Ini adalah tipe data teks/string"
    number = 3  # Tipe data angka, ada integer (bilangan bulat), ada float (bilangan desimal)
    nilai_integer = int(2.9)  # mengubah data menjadi integer (bilangan bulat)
    nilai_float = float("3")  # mengubah data menjadi float
    complex = 2j + 1  # Tipe data kompleks  (-2)^2  =  positif,  sqrt(-1) = bilangan kompleks
    boolean = False  # Hanya ada dua nilai, True atau False. biasa dipakai pada pengkondisian logic, seperti if statement
    tipe_data_none = None  # tipe data kosong, tidak ada nilai. (None berbeda dengan 0, berbeda juga dengan False)
    binary = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgwnLpRPAAA'  # contoh = base64 sebagai gambar
    list = [1, 2, 3]  # nilai lebih dari satu
    contoh_list = [  # [[jumlah siswa, tinggi badan]]
        [3, 160],
        [5, 180]
    ]

    contoh_tuple = (  # nilai lebih dari satu
        (3, 168),
        (5, 177)
    )

    contoh_dict = {  # ada konteks, biasa dipakai di restful api (dalam bentuk json)
        'nama': 'budi',
        'alamat': 'depok',
        'tinggi_badan': 170
    }

    listt = [  # tidak ada konteks, walaupun secara fungsional bisa
        ['budi', 'depok', 170]
    ]


    # jumlah siswa | tinggi badan
    # 1            | 160
    # 5            | 167
    # 8            | 180


    print("5 < 10? " + str(5 < 10))  # 5 < 10 adalah operator logika, sehingga menghasilkan nilai True atau False
    print("5 > 10? " + str(5 > 10)) # "a" + 5 = str + int  x(tidak bisa berjalan)
    
