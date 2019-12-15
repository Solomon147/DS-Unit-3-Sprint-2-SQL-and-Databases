#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import sqlite, create and connect to data file 
import sqlite3


# In[2]:


conn = sqlite3.connect('demo_data.sqlite3')


# In[3]:


curs = conn.cursor()


# In[4]:


#create a table
def nbm_create():
    b = '''CREATE TABLE demo(
        s text NOT NULL,
        x integer NOT NULL,
        y integer NOT NULL
    )'''
    curs.execute(b)


# In[5]:


nbm_create()


# In[6]:


#add DATA ROWS TO THE TABLE 
def nbm_insert():
    b1 = '''INSERT INTO demo VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)'''
    curs.execute(b1)


# In[7]:


nbm_insert()


# In[8]:


#saving my data table
def nbm_save():
    conn.commit()
    
nbm_save()


# In[9]:


#Count Rows
def row_count():
    a2 = '''
    SELECT COUNT (s)
    FROM demo
    '''
    curs.execute(a2)
    return curs.fetchall()

row_count()


# In[10]:


#Count rows greater than 5
def min_count():
    p1 = '''
    SELECT COUNT(*)
    FROM demo
    WHERE x >=5 and y>=5
    '''
    curs.execute(p1)
    return curs.fetchall()

min_count()


# In[11]:


#Count Unique y Values
def unique_count():
    a4 = '''
    SELECT COUNT(DISTINCT y)
    FROM demo
    '''
    curs.execute(a4)
    return curs.fetchall()

unique_count()


# In[ ]:




