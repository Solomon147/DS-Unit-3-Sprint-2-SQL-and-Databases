{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import sqlite3 and create and connect to data file\n",
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = sqlite3.connect('northwind_small.sqlite3')\n",
    "curs = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Côte de Blaye', 263.5, 18),\n",
       " ('Thüringer Rostbratwurst', 123.79, 12),\n",
       " ('Mishi Kobe Niku', 97, 4),\n",
       " (\"Sir Rodney's Marmalade\", 81, 8),\n",
       " ('Carnarvon Tigers', 62.5, 7),\n",
       " ('Raclette Courdavault', 55, 28),\n",
       " ('Manjimup Dried Apples', 53, 24),\n",
       " ('Tarte au sucre', 49.3, 29),\n",
       " ('Ipoh Coffee', 46, 20),\n",
       " ('Rössle Sauerkraut', 45.6, 12)]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#10 most expensive items\n",
    "def most_exp():\n",
    "    b = '''\n",
    "    SELECT ProductName, UnitPrice, SupplierId\n",
    "    FROM Product\n",
    "    ORDER BY UnitPrice DESC\n",
    "    LIMIT 10'''\n",
    "    curs.execute(b)\n",
    "    return curs.fetchall()\n",
    "\n",
    "most_exp()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(37.22222222222222,)]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Average hire age\n",
    "def avg_age():\n",
    "    a2 = '''\n",
    "    SELECT AVG\n",
    "    (HireDate - BirthDate)\n",
    "    FROM Employee\n",
    "    '''\n",
    "    curs.execute(a2)\n",
    "    return curs.fetchall()\n",
    "\n",
    "avg_age()\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),\n",
       " ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),\n",
       " ('Mishi Kobe Niku', 97, 'Tokyo Traders'),\n",
       " (\"Sir Rodney's Marmalade\", 81, 'Specialty Biscuits, Ltd.'),\n",
       " ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),\n",
       " ('Raclette Courdavault', 55, 'Gai pâturage'),\n",
       " ('Manjimup Dried Apples', 53, \"G'day, Mate\"),\n",
       " ('Tarte au sucre', 49.3, \"Forêts d'érables\"),\n",
       " ('Ipoh Coffee', 46, 'Leka Trading'),\n",
       " ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#add supp names to top 10\n",
    "def sup_name():\n",
    "    g = \"\"\"\n",
    "    SELECT \n",
    "    Product.ProductName AS  \"ProductName\",\n",
    "    Product.UnitPrice AS Price,\n",
    "    Supplier.CompanyName AS \"SupplierName\"\n",
    "    FROM Product, Supplier\n",
    "    WHERE Product.SupplierId = Supplier.Id\n",
    "    ORDER BY UnitPrice DESC\n",
    "    LIMIT 10\n",
    "    \"\"\"\n",
    "    curs.execute(g)\n",
    "    return curs.fetchall()\n",
    "\n",
    "sup_name()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Confections',)]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#finding the largest category\n",
    "def largest_cat():\n",
    "    a2 = \"\"\"\n",
    "    SELECT CategoryName\n",
    "    FROM Category\n",
    "    WHERE Id = (\n",
    "    SELECT Product.CategoryId\n",
    "    FROM Product\n",
    "    GROUP BY Product.categoryId\n",
    "    ORDER BY COUNT(Product.ProductName)DESC\n",
    "    LIMIT 1)\n",
    "    \"\"\"\n",
    "    curs.execute(a2)\n",
    "    return curs.fetchall()\n",
    "\n",
    "largest_cat()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
