from functools import reduce


if __name__ == '__main__':
    data1 = [
        ['Alice', 80],
        ['Bob', 90],
        ['Charlie', 85],
        ['Donny', 70]
    ]

    data2 = [
        80,
        90,
        85,
        70
    ]

    # Fungsi pengolahan data untuk jenis data list/array
    # 1. Map
    # 2. Filter
    # 3. Sort
    # 4. Reduce

    # Map: Mengubah elemen list ke dalam bentuk lain
    # Contoh: nilai ujian dibagi dua
    def bagi_dua(n):
        # n = iterator
        if n >= 80:
            return n/3
        return n/2

    # mapped_data = list(map(bagi_dua, data2))
    mapped_data = list(
            map(lambda n: n/2, data2)
        )

    # Filter: mengambil data yang dibutuhkan sesuai dengan kriteria
    # Contoh: ambil data yang nilainya 80 atau lebih
    def lebih_dari_80(n):
        # mengembalikan nilai boolean (True/False)
        return n >= 80

    # filtered_data = list(
    #     filter(lebih_dari_80, data2)
    # )
    filtered_data = list(
        filter(lambda n: n >= 80, data2)
    )

    # Sort: sortir list/array
    # Contoh: menyortir nilai dari terkecil ke besar
    sorted_data = list(
        sorted(data2, key=lambda n: n, reverse=False)
    )

    # Reduce: fungsi agregat (jumlah, rata-rata, max, min, median, std deviasi, dst)
    # Contoh: total nilai
    total = reduce(lambda x, y: x + y, data2)
    print(data2)
    print(f'total = {total}')

    # Contoh: rata-rata
    # N = Jumlah data (4)
    # n1, n2,... = element
    # rata-rata = n1/N + n2/N + ...
    # expect = 81.25
    N = len(data2)
    data2_mapped = map(lambda x: x/N, data2)
    average = reduce(lambda x, y: x + y, data2_mapped)
    print(f'average = {average}')

    # create_date = tanggal data/record dibuat
