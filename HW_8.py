import sqlite3
# Создать таблицу countries (страны) c колонками id первичный ключ автоинкрементируемый
# и колонка title с текстовым не пустым названием страны
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
        conn.commit() # commit после создания таблицы
    except sqlite3.Error as e:
        print(e)

# Создание полей в таблице
def insert_country(conn, country):
    sql = '''INSERT INTO countries 
    (title)
    VALUES(?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (country,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def insert_city(conn, city):
    sql = '''INSERT INTO cities 
    (title, area, country_id)
    VALUES(?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (city))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def insert_employee(conn, employee):
    sql = '''INSERT INTO employees
    (first_name, last_name, city_id)
    VALUES(?, ?, ?)    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (employee))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


connection = create_connection('hw_8.db')
sql_create_countries_table = '''
    CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL
    ) 
'''

sql_create_cities_table = '''
    CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    area FLOAT NOT NULL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (id)
    ) 
'''

sql_create_employees_table = '''
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities (id)
    )
'''


if connection is not None:
    print('Successfully connected!')
    # create_table(connection, sql_create_countries_table)
    # insert_country(connection, 'Kyrgyzstan')
    # insert_country(connection, 'Kazakhstan')
    # insert_country(connection, 'Germany')
    # insert_country(connection, 'Russia')
    # insert_country(connection, 'Japan')
    # insert_country(connection, 'China')
    # insert_country(connection, 'USA')

    # create_table(connection, sql_create_cities_table)
    # insert_city(connection,('Bishkek', 127000, 1))
    # insert_city(connection, ('Almaty', 682000, 2))
    # insert_city(connection, ('Berlin', 891800, 3))
    # insert_city(connection, ('Moscow', 2511000, 4))
    # insert_city(connection, ('Tokio', 2194000, 5))
    # insert_city(connection, ('Pekin', 16411000, 6))
    # insert_city(connection, ('New York', 783800, 7))

    # create_table(connection, sql_create_employees_table)
    # insert_employee(connection, ('James', 'Bond', 1))
    # insert_employee(connection, ('Jonny', 'Depp', 1))
    # insert_employee(connection, ('Don', 'Carleone', 2))
    # insert_employee(connection, ('Tony', 'Brasco', 2))
    # insert_employee(connection, ('Celine', 'Dion', 3))
    # insert_employee(connection, ('Jessica', 'Simpson', 3))
    # insert_employee(connection, ('Britney', 'Spears', 4))
    # insert_employee(connection, ('Mia', 'Khalifa', 4))
    # insert_employee(connection, ('Tom', 'Hardi', 5))
    # insert_employee(connection, ('Leonardo', 'DiCaprio', 5))
    # insert_employee(connection, ('Jack', 'Nickolson', 6))
    # insert_employee(connection, ('Jacky', 'Chan', 6))
    # insert_employee(connection, ('Halle', 'Berry', 7))
    # insert_employee(connection, ('Tom', 'Cruse', 7))
    # insert_employee(connection, ('Brad', 'Pitt', 7))

    connection.close()

# Написать программу в Python, которая при запуске бы отображала фразу “Вы можете отобразить список сотрудников
# по выбранному id города из перечня городов ниже, для выхода из программы введите 0:”
conn = sqlite3.connect('hw_8.db')
cursor = conn.cursor()

cursor.execute('SELECT id, title FROM cities')
cities = cursor.fetchall()

print(
    'You can display a list of employees by the selected city id from the list of cities below, to exit the program, enter 0:')
for city in cities:
    print(f'{city[0]}. {city[1]}')

while True:
    selected_city_id = int(input('Enter city id: '))

    if selected_city_id == 0:
        break
    if selected_city_id not in [city[0] for city in cities]:
        print('Error: The city with the specified ID was not found.')
        continue

    cursor.execute('''
        SELECT e.first_name, e.last_name, c.title, co.title, c.area
        FROM employees AS e
        JOIN cities AS c ON e.city_id = c.id
        JOIN countries AS co ON c.country_id = co.id
        WHERE c.id = ?
    ''', (selected_city_id,))

# После ввода определенного id города программа должна найти всех сотрудников из вашей базы данных
# проживающих в городе выбранного пользователем и отобразить информацию о них в консоли
    employees = cursor.fetchall()

    if not employees:
        print('There are no employees in this city.')
    else:
        print(f'Employees in this city:')
        for employee in employees:
            print(
                f'EMPLOYEE: {employee[0]} {employee[1]}, COUNTRY: {employee[3]}, '
                f'CITY: {employee[2]}, AREA: {employee[4]}')

conn.close()