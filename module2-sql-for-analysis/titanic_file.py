import pandas as pd
import sqlite3
import psycopg2

"""Remove (') from names"""
df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", " ")

"""Make sqlite3 file and connect to cursor"""
conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()

"""data from df to sql file"""
df.to_sql('titanic', conn, index=False, if_exists = 'replace')

"""Look at datatable and dattypes"""
big_curs = conn.cursor()
query = 'SELECT COUNT(*) FROM titanic;'
big_curs.execute(query).fetchall()

titanic = x_curs.execute('SELECT * FROM titanic;').fetchall()
big_curs.execute('PRAGMA table_info(titanic);').fetchall()

"""Connect psycopg2"""
dbname = 'qichvynf'
user = 'qichvynf'
password = '6Ay048Paw77VGp8l_UZaPbe0OGXLnBE6'
host = 'rajje.db.elephantsql.com'

nbm_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

nbm_conn
nbm_curs = nbm_conn.cursor()

"""Create table and execute"""
titanic_table = """
    CREATE TABLE titanic (
        index SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name TEXT,
        Sex TEXt,
        Age REAL,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Abroad INT,
        Fare REAL
);
"""
nbm_curs.execute(titanic_table)

"""Insert"""
for t in titanic:
    insert_titanic = """
      INSERT INTO titanic
      (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Abroad, Fare)
        VALUES """ + str(titanic[1:]) + ';'
    pg_curs.execute(insert_titanic)

pg_curs.execute('SELECT * FROM titanic;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()
