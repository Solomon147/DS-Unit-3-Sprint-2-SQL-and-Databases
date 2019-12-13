{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import sqlite, create and connect to data file \n",
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = sqlite3.connect('demo_data.sqlite3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "curs = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create a table\n",
    "def nbm_create():\n",
    "    b = '''CREATE TABLE demo(\n",
    "        s text NOT NULL,\n",
    "        x integer NOT NULL,\n",
    "        y integer NOT NULL\n",
    "    )'''\n",
    "    curs.execute(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "nbm_create()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#add DATA ROWS TO THE TABLE \n",
    "def nbm_insert():\n",
    "    b1 = '''INSERT INTO demo VALUES\n",
    "    ('g', 3, 9),\n",
    "    ('v', 5, 7),\n",
    "    ('f', 8, 7)'''\n",
    "    curs.execute(b1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "nbm_insert()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#saving my data table\n",
    "def nbm_save():\n",
    "    conn.commit()\n",
    "    \n",
    "nbm_save()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(3,)]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count Rows\n",
    "def row_count():\n",
    "    a2 = '''\n",
    "    SELECT COUNT (s)\n",
    "    FROM demo\n",
    "    '''\n",
    "    curs.execute(a2)\n",
    "    return curs.fetchall()\n",
    "\n",
    "row_count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(2,)]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count rows greater than 5\n",
    "def min_count():\n",
    "    p1 = '''\n",
    "    SELECT COUNT(*)\n",
    "    FROM demo\n",
    "    WHERE x >=5 and y>=5\n",
    "    '''\n",
    "    curs.execute(p1)\n",
    "    return curs.fetchall()\n",
    "\n",
    "min_count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(2,)]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count Unique y Values\n",
    "def unique_count():\n",
    "    a4 = '''\n",
    "    SELECT COUNT(DISTINCT y)\n",
    "    FROM demo\n",
    "    '''\n",
    "    curs.execute(a4)\n",
    "    return curs.fetchall()\n",
    "\n",
    "unique_count()"
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
