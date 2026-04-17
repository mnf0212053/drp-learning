import fungsi  # dependensi / modul
import dependensi_lain.pengurangan as pgr  # alias / nama lain
import numpy  # modul 3rd party (non-custom)

print('Inisiasi program')
print('===========================')

L = fungsi.add_tanpa_argumen()

print('Hasil penjumlahan: ', L)

M = fungsi.add_dengan_argumen(3, 9)

print('Hasil penjumlahan: ', M)

N = pgr.pengurangan(8, 6)

print('Hasil Pengurangan:', N)