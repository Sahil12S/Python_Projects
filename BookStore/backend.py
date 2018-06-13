#############################################################
#   Project:    OOP style for BookStore BackENd			    #
#   Author:     Sahil Sharma								#
#   Reference:  Udemy										#
#   Started on: June 12, 2017								#
#############################################################

import sqlite3


class Database:

	# Constructor
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT,  YEAR INTEGER, isbn INTEGER )")
		self.conn.commit()

	def insert(self, title, author, year, isbn):
		self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
		self.conn.commit()

	def view(self):
		self.cur.execute("SELECT * FROM book")
		rows = self.cur.fetchall()
		return rows

	def search(self, title="", author="", year="", isbn=""):
		self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
		rows = self.cur.fetchall()
		return rows

	def delete(self, id):
		self.cur.execute("DELETE FROM book WHERE id=?", (id,))
		self.conn.commit()

	def update(self, id, title, author, year, isbn):
		self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
		self.conn.commit()

	def __del__(self):
		self.conn.close()

# insert("The Earth", "John Smith", 1920, 191298323412)
# update(1, "The Sea Lion", "John Tablet", 1918, 19123232313412)
# print(view())
# print(search(author="John Tablet"))

# Gone Girl Gyllian Flynn 2012 0307588371
# Before I Go to Sleep S. J. Watson 2011 0062060563
# The Girl on the Train Paula Hawkins 2015 0735212169
# The Girl with All the Gifts Mike Carey 2014 0356502848
