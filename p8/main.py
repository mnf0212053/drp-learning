import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
mydb = client['mydb'] #  Inisiasi database
users = mydb['users']

if __name__ == '__main__':
    nama = input('masukkan nama: ')
    umur = input('masukkan umur: ')

    mydict = {
        'nama': nama,
        'umur': umur
    }

    data = users.insert_one(mydict)
    print(data.inserted_id)