import json
# Penyimpanan Data
# 1. File-based storage (csv (comma separated values), json, txt (tidak terstruktur), xls)
# 2. SQL (Structured Query Language, digunakan dalam DBMS (Database Management System) seperti Postgresql, Mysql, dll.)
# 3. NoSQL


def _load_data():
    with open('data.json', 'r') as f: #  r = read
        data = json.load(f)
    return data

def load_data():
    data = _load_data() #  fungsi utama
    print(data)

def save_data():
    nama = input('masukkan nama: ')
    umur = input('masukkan umur: ')

    data = _load_data()
    data.append({
        'nama': nama,
        'umur': umur
    })

    with open('data.json', 'w') as f: # w = write
        json.dump(data, f)

def delete_data():
    nama = input('masukkan nama yang akan dihapus: ')

    data = _load_data()
    d = list(filter(lambda x: x['nama'] == nama, data))
    if d:
        data.remove(d[0])

    with open('data.json', 'w') as f: # w = write
        json.dump(data, f)

if __name__ == '__main__':
    while True:
        print('Menu:')
        print('1. Load Data')
        print('2. Save Data')
        print('3. Delete Data')
        menu = input('menu: ')

        if menu == '1':
            load_data()
        elif menu == '2':
            save_data()
        elif menu == '3':
            delete_data()