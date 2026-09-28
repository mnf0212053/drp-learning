# Penjumlahan untuk tipe data numerik
x = 3.14
y = 1.1

a = x + y  # -> Penjumlahan matematis

# Penjumlahan untuk tipe data string
nama_awal = "John"
nama_akhir = "smith"
nama_tengah = "jackson"

nama_lengkap = nama_awal + nama_akhir  # -> Penggabungan

tinggi_1 = [180]
tinggi_2 = [190]

tinggi_total = tinggi_1 + tinggi_2  # -> ??

# list -> tipe data koleksi

sales_order = {
    'id': 1,
    'no_so': 'ABC1235',
    'product_name': 'Pulpen',
    'price_unit': 3000,
    'qty': 5
}

# list of dictionary
orders = [
    {
        'id': 1,
        'no_so': 'ABC1235',
        'product_name': 'Pulpen',
        'price_unit': 3000,
        'qty': 5
    },
    {
        'id': 2,
        'no_so': 'ABC1240',
        'product_name': 'Penggaris',
        'price_unit': 10000,
        'qty': 3
    }
]

# Running Python:
# 1. Klik kanan pada folder/direktori pada explorer, lalu pilih copy path pada file python yang akan dirun
# 2. Pada terminal, ketik "python " lalu paste path ke terminal menggunakan ctrl + v atau klik kanan pada terminal
# Perintah running python -> python <path file python>
# Contoh perintah untuk running python :
# python C:\Users\mnurf\Documents\Projects\work\drp\125\p4\main.py

# Perintah untuk mencetak tulisan ke dalam terminal (print statement):
# Sintaks -> print(<teks yang akan dicetak>)

# Contoh
# print("Hello world")  # cetak tulisan tanpa variabel

# message = "Hello world"
# print(message)  # cetak tulisan dengan variabel

umur = 20
print(umur)
