from sqlite3 import *
from sqlite3 import Error
from os import *
import random
from datetime import datetime, timedelta

def create_connect(path:str):
    connection=None 
    try:
        connection=connect(path)
        print("Ühendus on olemas!")
    except Error as e:
        print(f"Tekkis viga: {e}")
    return connection

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud või andmed on sisestatud")
    except Error as e:
        print(f"Tekkis viga: {e}")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None 
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Tekkis viga: {e}")

def execute_insert_query(connection, data):
    query = "INSERT INTO users(Name, Lastname, DateOfBirth, Age, GenderId, Nationality) VALUES(?,?,?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

def update_column_name(connection, table_name, current_column_name, new_column_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns_info = cursor.fetchall()
        column_exists = False
        for column in columns_info:
            if column[1] == current_column_name:
                column_exists = True
                break
        if column_exists:
            cursor.execute(f"ALTER TABLE {table_name} RENAME COLUMN {current_column_name} TO {new_column_name}")
            connection.commit()  # Добавлен вызов commit() для сохранения изменений
            print(f"Название столбца {current_column_name} в таблице {table_name} успешно обновлено на {new_column_name}")
        else:
            print(f"Столбец {current_column_name} не найден в таблице {table_name}")
    except Error as e:
        print(f"Ошибка при обновлении названия столбца: {e}")

def dropTable(connection, table):
    try:
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        connection.commit()
        #print("Tabel on kustutatud.")
    except Error as e:
        print(f"Tekkis viga: {e}")

def generate_random_user():
    names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Emma']
    lastnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']
    nationalities = ['USA', 'UK', 'Canada', 'Australia', 'Germany']

    name = random.choice(names)
    lastname = random.choice(lastnames)
    nationality = random.choice(nationalities)

    birthdate = datetime.now() - timedelta(days=random.randint(365*18, 365*60))
    age = datetime.now().year - birthdate.year

    gender_id = random.randint(1, 2)

    return (name, lastname, birthdate.strftime('%Y-%m-%d'), age, gender_id, nationality)

def auto_insert_users(connection, num_users):
    for i in range(num_users):
        user_data = generate_random_user()
        execute_insert_query(connection, user_data)

# Пример использования:
filename = path.abspath(__file__)
dbdir = filename.rstrip('Too_andmebaasiga.py')
dbpath = path.join(dbdir, "data.db")
conn = create_connect(dbpath)

create_users_table = """
CREATE TABLE IF NOT EXISTS users(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Lastname TEXT NOT NULL,
DateOfBirth DATETIME,
Age INTEGER,
Nationality TEXT,
GenderId INTEGER,
FOREIGN KEY (GenderId) REFERENCES gender(Id)
)
"""
create_gender_table = "CREATE TABLE IF NOT EXISTS gender(Id INTEGER PRIMARY KEY AUTOINCREMENT, Nimetus TEXT NOT NULL)"
insert_users = """
INSERT INTO
users(Name,Lastname,DateOfBirth,Age,GenderId,Nationality)
VALUES
('Vsevolod','Tsarev','2007-09-11',16,1,'Eesti'),
('Lev','Jegorov','2005-06-28',18,1,'Russia'),
('Kati','Smith','1998-05-13',26,2,'USA'),
('Martin','Sild','2002-09-11',22,1,'England'),
('Valeria','Sotsjova','2001-07-12',23,2,'Denmark')
"""
insert_gender = "INSERT INTO gender(Nimetus) VALUES ('mees'), ('naine')"
select_users = "SELECT * FROM users"
select_users_gender = "SELECT users.Name, Lastname, gender.Nimetus FROM users INNER JOIN gender ON users.GenderId=gender.Id"

execute_query(conn, create_gender_table)
execute_query(conn, insert_gender)
execute_query(conn, create_users_table)
execute_query(conn, insert_users)

# Обновление названия столбца
update_column_name(conn, "users", "Birthday", "DateOfBirth")

insert_user = (input("Eesnimi:"), input("Perenimi:"), input("Sünnikuupäev (YYYY-MM-DD): "), int(input("Vanus:")), int(input("Sugu (1 - mees, 2 - naine): ")), input("Rahvus: "))


num_new_users = int(input("Введите количество пользователей для добавления: "))
auto_insert_users(conn, num_new_users)

users = execute_read_query(conn, select_users)
print("Kautajate tabel 1:")
for user in users:
    print(user)

genders = execute_read_query(conn, select_users_gender)
print("Kautajate tabel 2:")
for gender in genders:
    print(gender)