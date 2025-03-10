# -*- coding: utf-8 -*-
"""creatingATable.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xeZtP1XaE-hB5N3VN5M_MG4bePTxO7DL
"""

#pip install psycopg2 #install the package

import psycopg2 #imported the package
dir(psycopg2)#its a good habit to look into the directory once you just downloaded a new package

help(psycopg2.connect)

help(psycopg2.extensions) #just to see the help

dbname ='qichvynf' #We entered them in here cos we are going to need them for the connector
user ='qichvynf'   #because we need a password to get into the database
password ='6Ay048Paw77VGp8l_UZaPbe0OGXLnBE6'
host = 'rajje.db.elephantsql.com'

"""We are going to open up a connector to a database. Typically we call connector conn but part of today's lesson, we are gonna open up a connector to enter sequel. Then we are gonna open up another connector to a enter a sequel like database with rpg characters in it(database in it) and we are going to move stuffs from one database to another. we are going to move stuffs from the sqlite(RPG stuff) into the other."""

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host) #open up a connector

pg_curs = pg_conn.cursor() #Now we create a cursor after creating a connector at the top. the cursor keeps track of where you're in the database. Helps us navigate the rows

pg_curs.execute('SELECT * FROM test_table;') #test_table from the elephantsql

pg_curs.fetchall() #this is the command to see the results

"""The first objective which is above is connecting to post test data base and now we move to the second objective. The 2nd objective is creating a data pipeline. pipeline been something that takes something from point a to point b. so we are going to pull sqlite database, transform(change it in our python script). and move it to the elephant sequel database"""

#next part. we are download our sequel like databse. Pulling it from github directly. and then modify it so that it has the right type.
#!wget https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true

#!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3                           #need to rename
#!ls -alh

import sqlite3 #we need to open up the connector and the cursor
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall()

sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character').fetchall() #so there are 5 names that were repeated

#pull out the character table in general and save it as a variable
characters = sl_curs.execute('SELECT * from charactercreator_character').fetchall()

characters[-1] #making sure the upper code worked correctly. By pulling up the last row. first row is [0]

#we could also look at length
len(characters)

# we need to see the types before we convert them. U execute statement ONTOP of the cursors.
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

create_character_table = """
  CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR (30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT);
"""

#if you run into an error, you've to close it and open it again. This is the code to do that.
#pg_curs.close() #closed the cursor
#pg_conn.commit() # commited the changes to the database
#pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host) #reopened connection
#pg_curs = pg_conn.cursor() #reopened the cursor

pg_curs.execute(create_character_table) #creating a table now

#now we are going to do one that would show the table(another query that shows the table)
show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

characters[0] #transforming the roles. chopping off the id number and turning it into a str in the next couple codes

str(characters[0][1:]) #this is just showing us

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisodm)
VALUES """ + str(characters[0][1:]);
print(example_insert) #we are printing it out cos we didn't want to run it because this just does one row and we need to do all of the rows. So we need to doa. forloop

#creating a forloop
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)

#try & see if that works
pg_curs.execute('SELECT * from charactercreator_character;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')

pg_characters = pg_curs.fetchall() #Just saving it to a variable so that we can compare it to know if they're identical

pg_characters #first list we have

#another list we have and we are just checking the three rows
characters[0:3]

#now we are going to compare them. and it says it passes cos it didn't give us an error after running it(Unittesing)
for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character

"""So basically this is how we move a table from one database to another and check if they're identical. Once we close and commit again, we can go back to our elephantsql to check. we figured out how to create a database in PostgreSQL(pg) and we also did our first data pipeline."""
