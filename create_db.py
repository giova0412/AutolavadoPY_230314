import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    port=3307
)

try:
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS autolavado_db;")
    connection.commit()
    print("Database created successfully")
finally:
    connection.close()
