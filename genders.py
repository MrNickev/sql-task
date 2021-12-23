import sqlite3

connection = sqlite3.connect("works.sqlite")
selector = connection.cursor()
selector.execute('drop table if exists genders')
selector.execute('create table genders ('
               'gender text primary key)')
selector.execute('insert into genders values("Мужской")')
selector.execute('insert into genders values("Женский")')
print(selector.execute('select * from genders').fetchall())