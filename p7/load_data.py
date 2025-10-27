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

def search_umur(umur: int):
    query = "SELECT * FROM users WHERE umur = ?"

    cursor = conn.cursor()
    cursor.execute(query, (umur,))
    return cursor.fetchall()

def load_user():
    query = """
        SELECT * FROM users
    """

    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == '__main__':
    data = search_umur(5)

    print(data)