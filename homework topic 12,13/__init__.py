# '''
# 1. Создать таблицу с студентами в БД
# 2. Создать таблицу аудиторий в БД
# 3. *Сделать связь таблиц
# '''
# import psycopg2
#
# conn = psycopg2.connect(
#     dbname='new_base',
#     user='blackbloodyring',
#     password='20062005',
#     host='127.0.0.1',
#     port='5432', )
# # Создаем курсор для выполнения SQL-запросов
#
# cur = conn.cursor()
#
# cur.execute('''
#     CREATE TABLE students(
#         first_name VARCHAR(10),
#         last_name VARCHAR(10),
#         age  INT,
#         classroom_id INT
#     )
# ''')
#
# cur.execute('''
#     CREATE TABLE classrooms(
#     number  INT UNIQUE
#     )
# ''')
#
# cur.execute('''
#     INSERT INTO students (first_name, last_name, age, classroom_id)
#     VALUES
#         ('Имя1', 'Фамилия1', 20, 101),
#         ('Имя2', 'Фамилия2', 21, 102),
#         ('Имя3', 'Фамилия3', 22, 103),
#         ('Имя4', 'Фамилия4', 23, 104),
#         ('Имя5', 'Фамилия5', 24, 105)
# ''')
#
# cur.execute('''
#     INSERT INTO classrooms (number)
#     VALUES (101), (102), (103), (104), (105)
# ''')
#
# cur.execute('''
#     ALTER TABLE students
#     ADD CONSTRAINT a
#     FOREIGN KEY (classroom_id) REFERENCES classrooms (number)
#
#
# ''')
# # 1)ALTER TABLE, чтобы внести изменения в существующую таблицу 'students'.
# # 2)FOREIGN KEY (classroom_id) - это дополнительная часть команды, которая указывает, что мы создаем внешний ключ
# # 3)(foreign key) в таблице 'students'. Мы говорим, что столбец 'classroom_id' в таблице 'students' будет внешним ключом,
# # который ссылается на данные в другой таблице.
# # 4) REFERENCES classrooms (number) это часть команды, которая указывает, на какой столбец в другой таблице
# # ('classrooms') будет ссылаться внешний ключ В данном случае, мы говорим, что столбец 'classroom_id' в таблице
# # 'students' будет ссылаться на столбец 'number' в таблице 'classrooms'.
#
# conn.commit()
# cur.close()
# conn.close()


# '''
# 1. Создать БД  postgresql с двумя таблицами, соединить их JOINʼом
#
# '''
#
# import psycopg2
#
# # Подключение к PostgreSQL
# conn = psycopg2.connect(
#     dbname='new_base',
#     user='blackbloodyring',
#     password='20062005',
#     host='127.0.0.1',
#     port='5432', )
#
# # Создание курсора
# cur = conn.cursor()
#
# # Создание таблицы с именем и фамилией
# cur.execute("""
#     CREATE TABLE  names (
#         id serial PRIMARY KEY,
#         first_name VARCHAR(255),
#         last_name VARCHAR(255)
#     )
# """)
#
# # Создание таблицы с возрастом
# cur.execute("""
#     CREATE TABLE  ages (
#         id serial PRIMARY KEY,
#         age INT
#     )
# """)
#
# # Вставка данных в таблицу с именем и фамилией
# cur.execute('''
# INSERT INTO names(first_name, last_name)
#     VALUES
#         ('Имя1', 'Фамилия1'),
#         ('Имя2', 'Фамилия2')
#
# ''')
#
# # Вставка данных в таблицу с возрастом
# cur.execute('''
# INSERT INTO ages(age)
#     VALUES
#         (25),
#         (35)
#
# ''')
#
# # Сохранение изменений
# conn.commit()
#
# # Выполнение JOIN-запроса
# cur.execute("""
# CREATE TABLE result AS
# SELECT names.first_name, names.last_name, ages.age FROM names JOIN ages ON names.id = ages.id;
# """)
#
# conn.commit()
#
# # Закрытие соединения и курсора
# cur.close()
# conn.close()

'''
2. *Подключить функции к запросам
'''
import psycopg2

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname='test_base',
    user='blackbloodyring',
    password='20062005',
    host='127.0.0.1',
    port='5432',
)

# Создание курсора
cur = conn.cursor()

# Создание таблицы с именем и фамилией
cur.execute("""
    CREATE TABLE  names (
        id serial PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255)
    )
""")

# Создание таблицы с возрастом
cur.execute("""
    CREATE TABLE  ages (
        id serial PRIMARY KEY,
        age INT
    )
""")

# Вставка данных в таблицу с именем и фамилией
cur.execute('''
INSERT INTO names(first_name, last_name)
    VALUES
        ('Имя1', 'Фамилия1'),
        ('Имя2', 'Фамилия2')
''')

# Вставка данных в таблицу с возрастом
cur.execute('''
INSERT INTO ages(age)
    VALUES
        (25),
        (35)
''')

# Создание простой функции
cur.execute("""
CREATE FUNCTION get_data()
RETURNS TABLE (first_name VARCHAR(255), last_name VARCHAR(255), age INT) AS 
$$
BEGIN
    RETURN QUERY SELECT names.first_name, names.last_name, ages.age 
                 FROM names 
                 JOIN ages ON names.id = ages.id;
END;
$$ LANGUAGE plpgsql;
""")

# Вызов функции и получение результата
cur.execute('SELECT * FROM get_data();')
result = cur.fetchall()
print(result)


conn.commit()

# Закрытие соединения и курсора
cur.close()
conn.close()
