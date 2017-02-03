from tkinter import *
import sqlite3
from datetime import datetime

fmt = '%Y-%m-%d %H:%M:%S'

def create_db(self):
	print("CREATE DB: It is here")
	conn = sqlite3.connect('filecheck.db')
	with conn:
		cur = conn.cursor()
		cur.execute("CREATE TABLE if not exists last_file_check( " + 
			"ID INTEGER PRIMARY KEY AUTOINCREMENT, " +
			"check_stamp TIMESTAMP);")
		cur.execute("""SELECT * FROM last_file_check ORDER BY check_stamp DESC""")
		ts = datetime.timestamp(datetime.now())
		try:
			self.most_recent_file_check = cur.fetchone()[1]
			setMessage(self)
		except:
			self.most_recent_file_check = ts
			cur.execute("""INSERT INTO last_file_check (check_stamp) VALUES (?)""", (ts,))
			setMessage(self, 'There are no previous file checks with this database')
			pass
		conn.commit()
	conn.close()

def count_records(cur):
	count = ""
	cur.execute("""SELECT COUNT(*) FROM last_file_check""")
	count = cur.fetchone()[0]
	return cur,count

def first_run(self):
	conn = sqlite3.connect('filecheck.db')
	with conn:
		cur = conn.cursor()
		cur,count = count_records(cur)
		if count < 1:
			print
	conn.close()

def addToList(self):
	#if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
	conn = sqlite3.connect('filecheck.db')
	with conn:
		cursor = conn.cursor()
		val = datetime.timestamp(datetime.now())
		print(val)
		try: 
			cursor.execute("""INSERT INTO last_file_check (check_stamp) VALUES (?)""",(val,))
		except:
		 	self.message = 'There was an error trying to add the timestamp to the database.'
	conn.commit()
	conn.close()

def setMessage(self, x=None):
	if x is not None:
		self.message.set(x)
		self.check_the_time = self.checkTime()
	else:
		self.converted_time = datetime.fromtimestamp(self.most_recent_file_check)
		value = self.checkTime()
		if self.checkTime() > self.converted_time:
			self.check_the_time = self.checkTime()
			msg = '. You have checked in files within one day.'
		elif self.checkTime() < self.converted_time:
			self.check_the_time = self.converted_time
			msg = '. It has been over one day since you last copied any recently modified files.'
		else:
			print("SOMETHING IS WRONG")
		self.message.set("This is the most recent file check executed: " + str(self.converted_time.strftime(fmt)) + msg)


if __name__ == '__main__':
	pass