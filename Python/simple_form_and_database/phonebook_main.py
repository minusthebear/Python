from tkinter import *
from tkinter import messagebox
import tkinter as tk
import phonebook_gui
import phonebook_func
import sqlite3

class ParentWindow(Frame):
	def __init__(self, master, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)

		self.master = master
		self.master.minsize(600,400)
		self.master.maxsize(600,400)

		# phonebook_func is a windows function

		phonebook_func.center_window(self,600,400)
		self.master.title('The Tkiner Phonebook Demo')
		self.master.configure(bg="#F0F0F0")

		# is on Windows
		self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))

		phonebook_gui.load_gui(self)



if __name__ == "__main__":
	root = tk.Tk()
	App = ParentWindow(root)
	root.mainloop()
