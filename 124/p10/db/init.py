import sqlite3

def init_tables(connection):
    # inisasi tabel

    # membuat tabel "makanan" sebagai master data
    connection.execute(
        """
            CREATE TABLE IF NOT EXISTS makanan (
                id integer PRIMARY KEY AUTOINCREMENT,
                nama varchar(255) NOT NULL,
                rasa varchar(255),
                cara_dimasak varchar(255) NOT NULL
            );
        """
    )  # Menjalankan file sql

    connection.execute(
        """
            CREATE TABLE IF NOT EXISTS histori_makan (
                id integer PRIMARY KEY AUTOINCREMENT,
                makanan_id int NOT NULL,
                waktu_makan datetime NOT NULL
            );
        """
    )  # Menjalankan file sql

def init_db():
    # inisiasi DB
    connection = sqlite3.connect('makanan_logger.db')

    init_tables(connection)
    return connection