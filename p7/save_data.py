import json
from load_data import load_file

def save_data(nama: str, umur: str):
    data = {
        'nama': nama,
        'umur': umur
    }
    loaded_data = load_file() #  return list, sehingga dapat dilakukan append
    loaded_data.append(data) #  tambah data ke storage

    with open('data.json', 'w') as f:
        json.dump(loaded_data, f)
    

if __name__ == '__main__':
    nama = input("masukkan nama: ")
    umur = input("masukkan umur: ")

    save_data(nama, umur)