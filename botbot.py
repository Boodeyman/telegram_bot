import sqlite3

database = sqlite3.connect('test.db')
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS articles (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")
#cursor.execute("INSERT INTO articles VALUES ('Facebook is cool!', 'Facebook is realy cool!', 100, 'Luney')")
#cursor.execute("SELECT rowid, * FROM articles")
#print(cursor.fetchall())
database.commit()

user_login = input('Login: ')
user_password = input('Password: ')

cursor.execute("SELECT login FROM articles")
if cursor.fetchone() is None:
    cursor.execute(f"INSERT INTO articles VALUES (?, ?, ?)", (user_login, user_password, 0))
    database.commit()
    print('Вы зарегестрировались!')
else:
    print('Такая запись имеется!')
database.close()