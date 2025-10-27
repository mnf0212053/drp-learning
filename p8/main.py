import pymongo

connection = 'mongodb://localhost:27017/'
myclient = pymongo.MongoClient(connection)

if __name__ == '__main__': 
    mydb = myclient['mydatabase']
    user = mydb['users']

    data = {
        "nama": input('masukkan nama: '),
        "umur": input('masukkan umur: ')
    }

    data = user.insert_one(data)
    for u in user.find():
        print(u)
