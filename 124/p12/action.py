from sqlite3 import Connection

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
    query = """
        SELECT s.id, p.name, p.code, p.price_unit, s.qty, s.price_total FROM sales s
        INNER JOIN products p ON p.id = s.product_id
        WHERE p.id = ?; 
    """

    cr = conn.cursor()
    cr.execute(query, (product_id,))

    result = cr.fetchall()

    print('Sales ID | Nama Produk | Kode Produk (SKU) | Harga Satuan | Jumlah | Harga Total')
    for res in result:
        print(f'{res[0]} | {res[1]} | {res[2]} | {res[3]} | {res[4]} | {res[5]}')

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
        INSERT INTO sales (product_id, qty, price_total) VALUES (?, ?, ?)
    """

    conn.execute(query, (product_id, qty, price_total))
    conn.commit()

    print('Pembelian berhasil')

    return

def sales_list(conn: Connection):
    # INNER JOIN: Menghubungkan satu tabel dengan tabel yang lain berdasarkan kolom unik
    # dalam kasus ini, kolom product_id dalam tabel sales mengacu pada kolom id dalam tabel products

    query = """
        SELECT s.id, p.name, p.code, p.price_unit, s.qty, s.price_total FROM sales s
        INNER JOIN products p ON p.id = s.product_id; 
    """

    cr = conn.cursor()
    cr.execute(query)

    result = cr.fetchall()

    print('Sales ID | Nama Produk | Kode Produk (SKU) | Harga Satuan | Jumlah | Harga Total')
    for res in result:
        print(f'{res[0]} | {res[1]} | {res[2]} | {res[3]} | {res[4]} | {res[5]}')

