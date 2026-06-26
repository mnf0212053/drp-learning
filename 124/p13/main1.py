import csv
from functools import reduce

if __name__ == '__main__':
    filename = 'tahun-2021-cakupan-bayi-diimunisasi-polio.csv'

    with open(filename, newline='') as f:
        data = list(csv.reader(f))[1:7]

    print('Sebelum Mapping')
    print(data[0:5])

    # new_data = []
    # for d in data:
    #     new_data.append([d[1], d[2], int(d[5]) + int(d[6])])

    new_data = list(map(lambda d: [d[1], int(d[5]) + int(d[6])], data))

    print('Setelah Mapping')
    print(new_data[0:5])

    def total(x, y):
        kelurahan = 'Bukateja'

        if y[0] == kelurahan:
            return x + y[1]

        return x

    result = reduce(total, new_data, 0)

    print('Hasil')
    print(result)
    
