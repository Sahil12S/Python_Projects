#################################################################################
#   Project:    OOP style for BookStore FrontEnd    							#
#   Author:     Sahil Sharma                    								#
#   Reference:  Udemy                           								#
#   Started on: June 12, 2017                   								#
#   Other info: Venv: workspace/PythonEnvironments/pyinstaller                  #
#################################################################################

from tkinter import *
from backend import Database


database = Database("books.db")


class Window(object):

	def __init__(self, window):

		self.window = window

		self.window.wm_title("Bookstore")

		# Title - Label
		l1 = Label(window, text="Title")
		l1.grid(row=0, column=0)

		# Title - Entry
		self.title_val = StringVar()
		self.e1 = Entry(window, textvariable=self.title_val)
		self.e1.grid(row=0, column=1)

		# Author - Label
		l2 = Label(window, text="Author")
		l2.grid(row=0, column=2)

		# Author - Entry
		self.author_val = StringVar()
		self.e2 = Entry(window, textvariable=self.author_val)
		self.e2.grid(row=0, column=3)

		# Year - Label
		l3 = Label(window, text="Year")
		l3.grid(row=1, column=0)

		# Year - Entry
		self.year_val = StringVar()
		self.e3 = Entry(window, textvariable=self.year_val)
		self.e3.grid(row=1, column=1)

		# ISBN - Label
		l4 = Label(window, text="ISBN")
		l4.grid(row=1, column=2)

		# ISBN - Entry
		self.isbn_val = StringVar()
		self.e4 = Entry(window, textvariable=self.isbn_val)
		self.e4.grid(row=1, column=3)

		# List box
		self.list1 = Listbox(window, height=10, width=28)
		self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

		# Scroll bar
		sb1 = Scrollbar(window)
		sb1.grid(row=2, column=2, rowspan=6)

		# Configure scroll bar with list box
		self.list1.configure(yscrollcommand=sb1.set)
		sb1.configure(command=self.list1.yview)

		# Bind function to a widget event. Arg1: event-type. Arg2: function to bind to event
		self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

		# Button1: View All
		b1 = Button(window, text="View All", width=12, command=self.view_command)
		b1.grid(row=2, column=3)

		# Button2: Search Entry
		b2 = Button(window, text="Search Entry", width=12, command=self.search_command)
		b2.grid(row=3, column=3)

		# Button3: Add Entry
		b3 = Button(window, text="Add Entry", width=12, command=self.add_command)
		b3.grid(row=4, column=3)

		# Button4: Update
		b4 = Button(window, text="Update", width=12, command=self.update_command)
		b4.grid(row=5, column=3)

		# Button5: Delete
		b5 = Button(window, text="Delete", width=12, command=self.del_command)
		b5.grid(row=6, column=3)

		# Button6: Close
		b6 = Button(window, text="Close", width=12, command=window.destroy)
		b6.grid(row=7, column=3)

	def get_selected_row(self, event):
		try:
			index = self.list1.curselection()[0]
			self.selected_tuple = self.list1.get(index)
			self.e1.delete(0, END)
			self.e1.insert(END, self.selected_tuple[1])
			self.e2.delete(0, END)
			self.e2.insert(END, self.selected_tuple[2])
			self.e3.delete(0, END)
			self.e3.insert(END, self.selected_tuple[3])
			self.e4.delete(0, END)
			self.e4.insert(END, self.selected_tuple[4])
		except IndexError:
			pass

	# Function to display data in list box.
	def view_command(self):
		# make sure list box is empty every time button is clicked.
		self.list1.delete(0, END)
		for row in database.view():
			self.list1.insert(END, row)		# Insert at the end of existing row

	# Search book store according to user need.
	def search_command(self):
		self.list1.delete(0, END)
		for row in database.search(self.title_val.get(), self.author_val.get(), self.year_val.get(), self.isbn_val.get()):
			self.list1.insert(END, row)

	# Insert Entry in database
	def add_command(self):
		database.insert(self.title_val.get(), self.author_val.get(), self.year_val.get(), self.isbn_val.get())
		self.list1.delete(0, END)
		self.list1.insert(END, (self.title_val.get(), self.author_val.get(), self.year_val.get(), self.isbn_val.get()))

	# Delete an entry from Book Store.
	def del_command(self):
		database.delete(self.selected_tuple[0])

	# Delete an entry from Book Store.
	def update_command(self):
		database.update(self.selected_tuple[0], self.title_val.get(), self.author_val.get(), self.year_val.get(), self.isbn_val.get())


window = Tk()
Window(window)
window.mainloop()


###
# Notes:
# 	1. Creating executable file:
#		pyinstaller <filename.py>
###
