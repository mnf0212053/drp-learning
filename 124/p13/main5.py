from functools import reduce

if __name__ == '__main__':
    nilai_ujian = [
        70,
        80,
        60,
        60
    ]

    # tanpa mapreduce
    total_nilai = 0
    for nilai in nilai_ujian:
        total_nilai = total_nilai + nilai

    print(total_nilai)

    # dengan reduce
    total_nilai = reduce(lambda x, y: x + y, nilai_ujian)
    print(total_nilai)