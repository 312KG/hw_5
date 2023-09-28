import sqlite3

# Создание соединения с БД
def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


# Создание таблицы
def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Создание полей в таблице
def insert_product(conn, product):
    sql = '''INSERT INTO products 
    (product_title, price, quantity)
    VALUES(?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Добавить функцию, которая меняет количество товара по id
def update_product_quantity(conn, product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Добавить функцию, которая меняет цену товара по id
def update_product_price(conn, product):
    sql = '''UPDATE products SET price = ? WHERE id = ?    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

#Добавить функцию, которая удаляет товар по id
def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
def select_all_products(conn):
    sql = '''SELECT * FROM products    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

# Добавить функцию, которая бы выбирала из БД товары, которые дешевле 100 сомов
# и количество которых больше чем 5 и распечатывала бы их в консоли
def select_products_by_price_and_quantity(conn, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ?    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

# Добавить функцию, которая бы искала в БД товары по названию
def select_products_by_title(conn, keyword):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + keyword + '%',))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)



connection = create_connection('hw.db')
sql_create_products_table = '''
    CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,        
    quantity INTEGER NOT NULL DEFAULT 0
    )
'''


if connection is not None:
    print('Successfully connected!')
    # create_table(connection, sql_create_products_table)
    # insert_product(connection, ('Bread', 45.0, 120))
    # insert_product(connection, ('Bread Wheat', 47.25, 96))
    # insert_product(connection, ('Rice', 45.0, 120))
    # insert_product(connection, ('Waffle', 72.0, 150))
    # insert_product(connection, ('Yoghurt', 54.0, 375))
    # insert_product(connection, ('Milk', 90.86, 115))
    # insert_product(connection, ('Sour Cream', 117.0, 60))
    # insert_product(connection, ('Cottage cheese', 215.0, 70))
    # insert_product(connection, ('Butter', 124.0, 90))
    # insert_product(connection, ('Cheese', 218.0, 24))
    # insert_product(connection, ('Sugar', 55.6, 80))
    # insert_product(connection, ('Sugar Brown', 180.0, 50))
    # insert_product(connection, ('Chocolate', 570.0, 430))
    # insert_product(connection, ('Egg', 11.0, 800))
    # insert_product(connection, ('Meat', 580.0, 150))

# Протестировать каждую написанную функцию
    # update_product_quantity(connection, (57, 2))
    # update_product_price(connection, (555, 13))
    # delete_product(connection, 12)
    # select_all_products(connection)
    # select_products_by_price_and_quantity(connection, 100, 5)
    # select_products_by_title(connection, 'Bread')
    # select_products_by_title(connection, 'cheese')


    connection.close()