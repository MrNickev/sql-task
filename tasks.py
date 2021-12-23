import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect("works.sqlite")
cursor = connection.cursor()

#Выводит количество записей.

print(cursor.execute('select count(*) from works').fetchone()[0])  # 32683

#Выводит количество мужчин и женщин.

print(cursor.execute('select count(*) from works where gender = "Мужской"').fetchone()[0])  # 13386
print(cursor.execute('select count(*) from works where gender = "Женский"').fetchone()[0])  # 17910

#Количество заполненных skills

print(cursor.execute('select count(*) from works where skills != "None"').fetchone()[0])  # 8972

#Получить заполненные скиллы.

print(cursor.execute('select skills from works where skills != "None"').fetchone())

#Выводит зарплату людей, владеющих Python

print(cursor.execute('select count(*) from works where skills like "%Python%"').fetchone()[0])

#Строит перцентили и разброс по з/п у мужчин и женщин.

print(pd.read_sql('select salary from works where gender = "Мужской"', connection).describe()[3:].transpose())
print(pd.read_sql('select salary from works where gender = "Женский"', connection).describe()[3:].transpose())

# 9. Построить графики распределения по з/п мужчин и женщин (а также в зависимости от высшего образования).

for (gender, ed) in [(gender, ed)
                     for ed in ("Высшее", "Незаконченное высшее", "Среднее", "Среднее профессиональное")
                     for gender in ('Мужской', 'Женский')]:
    sql_query = f'select salary from works where gender = "{gender}" and educationType = "{ed}"'
    salary = [row[0] for row in cursor.execute(sql_query).fetchall()]
    plt.hist(salary, bins=100)
    plt.title(f'{gender} заработок с образованием "{ed}"')
    plt.show()