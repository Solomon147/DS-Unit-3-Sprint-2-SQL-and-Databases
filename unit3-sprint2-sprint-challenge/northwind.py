#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import sqlite3 and create and connect to data file
import sqlite3


# In[2]:


conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


# In[4]:


#10 most expensive items
def most_exp():
    b = '''
    SELECT ProductName, UnitPrice, SupplierId
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10'''
    curs.execute(b)
    return curs.fetchall()

most_exp()


# In[5]:


#Average hire age
def avg_age():
    a2 = '''
    SELECT AVG
    (HireDate - BirthDate)
    FROM Employee
    '''
    curs.execute(a2)
    return curs.fetchall()

avg_age()
    


# In[6]:


#add supp names to top 10
def sup_name():
    g = """
    SELECT 
    Product.ProductName AS  "ProductName",
    Product.UnitPrice AS Price,
    Supplier.CompanyName AS "SupplierName"
    FROM Product, Supplier
    WHERE Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10
    """
    curs.execute(g)
    return curs.fetchall()

sup_name()


# In[7]:


#finding the largest category
def largest_cat():
    a2 = """
    SELECT CategoryName
    FROM Category
    WHERE Id = (
    SELECT Product.CategoryId
    FROM Product
    GROUP BY Product.categoryId
    ORDER BY COUNT(Product.ProductName)DESC
    LIMIT 1)
    """
    curs.execute(a2)
    return curs.fetchall()

largest_cat()


# In[ ]:




