import sqlite3


# Connect to database
conn = sqlite3.connect('data.db')

# Create table
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               nama TEXT,
               umur INTEGER
               )""")

def save_user(nama: str, umur: str):
    query = """
        INSERT INTO users ('nama', 'umur') VALUES (?, ?)
    """

    cursor = conn.cursor()
    cursor.execute(query, (nama, umur))
    conn.commit()

if __name__ == '__main__':
    nama = input('masukkan nama: ')
    umur = input('masukkan umur: ')

    save_user(nama, umur)