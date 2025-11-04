import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
mydb = client['mydb'] #  Inisiasi database
users = mydb['users']

if __name__ == '__main__':
    # nama = input('masukkan nama: ')
    # umur = input('masukkan umur: ')

    # mydict = {
    #     'nama': nama,
    #     'umur': umur
    # }

    # data = users.insert_one(mydict)  #  Memasukkan data/record ke collection

    data = users.find_one() #  Mencari satu record ke collection, diambil nilai pertama

    data = users.find() #  Mencari lebih dari  satu record, sehingga perlu diiterasi untuk mendapatkan datanya
    # for d in data:
    #     print(d)

    query = {"umur": 20}  # case sensitive, "20" tidak sama dengan 20
    data = users.find(query)  # query data

    for d in data:
        print(d)