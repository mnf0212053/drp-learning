from sqlite3 import Connection
import json

import bcrypt

def register(conn: Connection):
    name = input('Nama: ')
    username = input('Username: ')
    password = input('Password: ')

    # Penyamaran password
    # Generate salt terlebih dahulu untuk randomisasi
    salt = bcrypt.gensalt()

    # samarkan password menggunakan salt yang sudah dibuat
    password_hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    query = """
        INSERT INTO users (name, username, password) VALUES (?, ?, ?)
    """
    conn.execute(query, (name, username, password_hashed))
    conn.commit()

    print('Akun berhasil didaftarkan.')
    return

def login(conn: Connection):
    username = input('Username: ')
    password = input('Password: ')

    # ambil password yang tersamarkan terlebih dahulu dalam db. id juga diambil sebagai token
    query = """
        SELECT id, password FROM users WHERE username = ?;
    """

    cr = conn.cursor()
    cr.execute(query, (username,))

    result = cr.fetchone()

    if not result:
        raise Exception('Login Gagal')

    password_hashed = result[1]

    if not bcrypt.checkpw(password.encode('utf-8'), password_hashed):
        raise Exception('Login Gagal')

    # biasanya user diidentifikasi melalui token yang ada di cookie browser, 
    # namun untuk mempermudah, kita buat file json untuk mensimulasikan cookie browser, kita simpan user id ke dalam file login.json
    with open('login.json', 'w') as f:
        json.dump({'id': result[0]}, f)
        f.close()

    print('Login berhasil!')
    return

def get_user_id():
    with open('login.json', 'r') as f:
        data = json.load(f)

    return data['id']

def users_list(conn: Connection):
    query = """
        SELECT id, name, username FROM users;
    """

    cr = conn.cursor()
    cr.execute(query)

    result = cr.fetchall()

    print('ID | Nama | Username')
    for res in result:
        print(f'{res[0]} | {res[1]} | {res[2]}')

def product_detail(conn: Connection):
    product_id = int(input('Masukkan ID Produk: '))
    query = """
        SELECT id, name, code, description, price_unit from products where id = ?
    """

    cr = conn.cursor()
    cr.execute(query, (product_id,))

    product = cr.fetchone()

    if not product:
        print('Produk tidak ditemukan.')
        return

    product = product[0]

    print('=========================================')
    print('DETAIL PRODUK')
    print(f'{product[1]} ({product[0]})')
    print(f'Kode SKU: {product[2]}')
    print(f'Harga Satuan: {product[4]}')
    print(f'Deskripsi: {product[3]}')
    print('=========================================')

    return

def sales_list_by_product(conn: Connection):
    product_id = int(input('Masukkan ID Produk: '))
    # s dan p adalah alias untuk 
    # products (id, name): (1, bakso) (2, sate)
    # sales (id, product_id) (1, 1)

    query = """
        SELECT s.id, u.name, p.name, p.code, p.price_unit, s.qty, s.price_total FROM sales s
        INNER JOIN products p ON p.id = s.product_id
        INNER JOIN users u ON u.id = s.user_id
        WHERE p.id = ?; 
    """

    cr = conn.cursor()
    cr.execute(query, (product_id,))

    result = cr.fetchall()

    print('Sales ID | Customer | Nama Produk | Kode Produk (SKU) | Harga Satuan | Jumlah | Harga Total')
    for res in result:
        print(f'{res[0]} | {res[1]} | {res[2]} | {res[3]} | {res[4]} | {res[5]} | {res[6]}')

def product_list(conn: Connection):
    query = """
        select id, name, code from products;
    """

    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()

    print('DAFTAR PRODUK')
    print('-------------------------')
    print('ID | Nama | Kode SKU')
    print('-------------------------')
    for res in result:
        print(f'{res[0]} | {res[1]} | {res[2]}')
    print('-------------------------')

def product_list_seller(conn: Connection):
    product_list(conn)
    
    # Tambah sub menu untuk detail produk
    print('1. Lihat Detail Produk')
    print('2. Buat Produk')
    print('3. List Penjualan per Produk')

    act = input('Masukkan Aksi: ')
    if act == '1':
        product_detail(conn)
    elif act == '2':
        product_create(conn)
    elif act == '3':
        sales_list_by_product(conn)

    return

def product_create(conn: Connection):
    name = input('Nama Produk: ')
    code = input('Kode Produk (SKU): ')
    price_unit = float(input('Harga Satuan: '))
    description = input('Deskripsi Produk: ')

    query = """
        INSERT INTO products ('name', 'code', 'description', 'price_unit') VALUES (?, ?, ?, ?); 
    """

    conn.execute(query, (name, code, description, price_unit))
    conn.commit()

    print('Produk berhasil dimasukkan.')

    return

def buy(conn: Connection):
    user_id = get_user_id()
    product_id = int(input('Masukkan ID produk yang akan dibeli: '))
    qty = int(input('Masukkan jumlah produk: '))

    # Olah data price_total = qty * harga satuan. 
    # harga satuan (price_unit) diperoleh dari tabel products, sehingga harus query terlebih dahulu
    query = "SELECT price_unit FROM products WHERE id = ?;"
    cr = conn.cursor()
    cr.execute(query, (product_id,))

    price_unit = cr.fetchone()

    if not price_unit:
        print('Produk tidak ditemukan.')
        return

    price_total = price_unit[0] * qty

    query = """
        INSERT INTO sales (user_id, product_id, qty, price_total) VALUES (?, ?, ?, ?)
    """

    conn.execute(query, (user_id, product_id, qty, price_total))
    conn.commit()

    print('Pembelian berhasil')

    return

def export_sales(conn: Connection):
    query = """
        SELECT s.id, p.name, p.code, p.price_unit, s.qty, s.price_total FROM sales s
        INNER JOIN products p ON p.id = s.product_id; 
    """

    cr = conn.cursor()
    cr.execute(query)

    result = cr.fetchall()

    list_result = []
    for res in result:
        list_result.append({ # type: ignore
            'id': res[0],
            'product_name': res[1],
            'product_code': res[2],
            'price_unit': res[3],
            'qty': res[4],
            'price_total': res[5]
        })

    with open('sales.json', 'w') as f:
        json.dump(list_result, f)
        f.close()

    print('Export berhasil.')

def sales_list(conn: Connection):
    # INNER JOIN: Menghubungkan satu tabel dengan tabel yang lain berdasarkan kolom unik
    # dalam kasus ini, kolom product_id dalam tabel sales mengacu pada kolom id dalam tabel products

    query = """
        SELECT s.id, u.name, p.name, p.code, p.price_unit, s.qty, s.price_total FROM sales s
        INNER JOIN products p ON p.id = s.product_id
        INNER JOIN users u ON u.id = s.user_id; 
    """

    cr = conn.cursor()
    cr.execute(query)

    result = cr.fetchall()

    print('Sales ID | Customer | Nama Produk | Kode Produk (SKU) | Harga Satuan | Jumlah | Harga Total')
    for res in result:
        print(f'{res[0]} | {res[1]} | {res[2]} | {res[3]} | {res[4]} | {res[5]} | {res[6]}')

