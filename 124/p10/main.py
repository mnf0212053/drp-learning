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

def display_menu():
    print('1. Tambah Data Makanan')
    print('2. Catat Histori Makan')

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

def manage_menu(connection, menu):
    if menu == '1':
        tambah_makanan(connection)
    elif menu == '2':
        pass
        # catat_histori(connection)


if __name__ == '__main__':
    connection = init_db()

    while True:
        display_menu()
        lihat_makanan(connection)

        menu = input('pilih menu: ')
        manage_menu(connection, menu)
