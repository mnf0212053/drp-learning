# ERD (Entity Relationship Diagram)

# Entity = Objek
# Contoh: 
# Aplikasi untuk mendata *makanan* yang telah dikonsumsi
# terdapat *histori* terkait apa yang dimakan dan kapan makanan itu dimakan

# Entitas = Makanan

# Tabel makanan (master data):
# id (1, 2, 3, dst) (PK, auto increment)
# nama (Rendang, Ayam, Telur, dst.)
# rasa (asin, manis, dst.)
# cara dimasak (digoreng, direbus, dst.)
# tanggal dibuat (05-06-2026)
# tanggal diedit (05-06-2026)
# user_create (user yang membuat data)
# user_edit (user yang edit data)

# Tabel histori_makan:
# id int not null (PK, auto increment)
# makanan_id int not null (FK, mengacu ke kolom id pada tabel makanan)
# waktu_makan datetime not null 

# Jika tabel histori_makan hanya mencatat satu jenis makanan saja, maka sifatnya many to one

# John Doe -> 8 karakter
# varchar(50) -> maksimal 50 karakter 

# PK = Primary Key (umumnya adalah id (integer))
# FK = Foreign Key

# Jenis Relasi:
# 1. Many to One
# 2. One to many
# 3. Many to many

# entitas: dosen, mahasiswa

# MNF:
# - kania
# - ainaya

# persepsi dosen: one to many ke mahasiswa
# persepsi mahasiswa: many to one ke dosen

from db.init import init_db
import json

def display_menu():
    print('1. Tambah Data Makanan')
    print('2. Catat Histori Makan')
    print('3. Ekspor Data Makanan')
    print('4. Impor Data Makanan')

def tambah_makanan(connection):
    # UI/UX
    print('Masukkan data-data makanan berikut')
    nama = input('Nama Makanan: ')
    rasa = input('Rasa :')
    cara_dimasak = input('Cara Dimasak: ')

    # masukkan query untuk memasukkan makanan ke dalam database (INSERT INTO)
    # TIDAK DIREKOMENDASIKAN MENGGUNAKAN CARA INI, KARENA BISA DISERANG MENGGUNAKAN SQL INJECTION
    cursor = connection.cursor()

    cursor.execute(
        """
            INSERT INTO makanan (nama, rasa, cara_dimasak)
            VALUES (?, ?, ?);
        """, (nama, rasa, cara_dimasak)
    )
    connection.commit()

    # yang seharusnya digunakan (prepared statement):
    # """
    #     INSERT INTO makanan (nama, rasa, cara_dimasak)
    #     VALUES (?, ?, ?);
    # """

    print('Data berhasil ditambah')

def lihat_makanan(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
            select * from makanan;
        """
    )

    print(cursor.fetchall())

def export_makanan(connection):
    query = """
        select id,nama,rasa,cara_dimasak from makanan;
    """

    cursor = connection.cursor()
    cursor.execute(query)

    hasil_query = cursor.fetchall()

    # ubah hasil query menjadi dict, saat ini hasilnya masih:
    # [(1, 'Rendang', 'Asin', 'Digoreng'), (2, 'Ayam', 'Manis', 'Dibakar'), (3, 'Nasi Goreng', 'Pedas', 'Digoreng')]

    hasil_query_dict = [] 
    # list kosong, dapat diisi menggunakan append
    for data in hasil_query:
        makanan_object = {
            'id': data[0],
            'nama': data[1],
            'rasa': data[2],
            'cara_dimasak': data[3]
        }

        # tambahkan makanan_object ke hasil_query_dict
        hasil_query_dict.append(makanan_object)

    # masukkan list "hasil_query_dict" ke dalam file json
    with open('makanan.json', 'w') as f:
        json.dump(hasil_query_dict, f)
        f.close()

    print('Ekspor data sudah selesai. Silahkan dilihat di file makanan.json')

    return

def import_makanan(connection):
    # ada 2 pendekatan
    # 1. Sertakan ID
    # file json
    # [
    #   {
    #      "id": 1,
    #      "nama": "Nasi"
    #   }
    # ]
    # karena ID adalah unique identifier, maka jika di dalam database terdapat record dengan ID yang sama, maka biasanya ada konflik
    # terkadang solusinya adalah record di dalam database akan tertimpa (overwrite) dengan data yang baru
    # 2. Tidak menyertakan ID
    # [
    #   {
    #      "nama": "Nasi"
    #   }
    # ]
    # karena tidak ada unique identifier, maka pada umumnya semua data yang akan diimport akan mengisi database (INSERT INTO)
    # ada kemungkinan data di dalam database akan mengalami duplikasi

    # Panggil file terlebih dahulu
    # r = read, w = write
    with open('makanan_import.json', 'r') as f:
        data = json.load(f)
        f.close()

    # cek terlebih dahulu ID data, jika ID sudah terpakai
    # maka record akan ditimpa dengan data baru

    # query untuk cek apakah id sudah ada
    # jika tidak ada, akan menghasilkan data kosong
    query_check_id = """
        SELECT id FROM makanan WHERE id = ?
    """

    # masukkan "data" ke dalam database
    query_create = """
        INSERT INTO makanan (nama, rasa, cara_dimasak) values (?, ?, ?)
    """

    # untuk query where, gunakan ID (unique identifier)
    # untuk dijadikan sebagai target edit
    # WHERE WAJIB
    query_update = """
        UPDATE makanan
        SET nama = ?, rasa = ?, cara_dimasak = ?
        WHERE id = ?; 
    """

    cursor = connection.cursor()

    # Karena "data" berbentuk list, maka harus diiterasi
    for d in data:
        # buat logic terlebih dahulu untuk menentukan apakah
        # data dicreate atau update
        # jika ID ada, maka update id tersebut
        # namun jika tidak ada, maka buat baru
        cursor.execute(query_check_id, (d['id'],))  # untuk tuple satu item, gunakan (data,)
        is_exist = cursor.fetchone()

        if is_exist:
            # update
            cursor.execute(query_update, (d['nama'], d['rasa'], d['cara_dimasak'], d['id']))
        else:
            # create
            cursor.execute(query_create, (d['nama'], d['rasa'], d['cara_dimasak']))

    connection.commit()
    print('Import data berhasil.')

def manage_menu(connection, menu):
    if menu == '1':
        tambah_makanan(connection)
    elif menu == '2':
        pass
        # catat_histori(connection)
    elif menu == '3':
        # Export data makanan dari database ke file json
        export_makanan(connection)
    elif menu == '4':
        import_makanan(connection)


if __name__ == '__main__':
    connection = init_db()

    while True:
        display_menu()
        lihat_makanan(connection)

        menu = input('pilih menu: ')
        manage_menu(connection, menu)
