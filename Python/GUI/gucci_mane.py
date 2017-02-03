from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import shutil
from datetime import datetime, timedelta

fmt = '%Y-%m-%d %H:%M:%S'
ext = '.py'

class MainApplication(ttk.Frame):

	def __init__(self, parent, *args, **kwargs):
		self.folders = {0: None, 1: None}
		counter = 0

		self.dir_opt = options = {}
		options['initialdir'] = os.getcwd()
		options['mustexist'] = False
		options['parent'] = root
		options['title'] = 'This is a title'

		ttk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.parent.minsize(600,400)
		self.parent.maxsize(600,400)
		self.center_window(600,400)

		self.intro_text = Label(self, height=5, wraplength=600, text=("Welcome to the Magical Move File Application! "
											"This will copy all files with extension .py and move "
											"them from and to any two folders of your choice! "
											"The application will only copy files modified within one day."))
		self.intro_text.grid(row=0, column=0, columnspan=2, pady=(0,10))
		
		self.btn_from = Button(self, width=12, height=2, text='From Folder', command=lambda: self.openDir(self.var1))
		self.btn_from.grid(row=1, column=0, padx=(25,0), pady=(60,10))
		self.btn_to = Button(self, width=12, height=2, text='To Folder', command=lambda: self.openDir(self.var2))
		self.btn_to.grid(row=1, column=1, padx=(25,0), pady=(60,10))
		self.btn_send = Button(self, width=12, height=2, text='Send all files', command=lambda: self.sendFiles())
		self.btn_send.grid(row=3, column=0, columnspan=2)

		self.var1 = StringVar()
		self.var2 = StringVar()

		self.entrytext_from = Entry(self, textvariable = self.var1)
		self.entrytext_from.grid(row=2, column=0, padx=(25,0), pady=(10,10), sticky='ew')
		self.entrytext_to = Entry(self, textvariable = self.var2)
		self.entrytext_to.grid(row=2, column=1, padx=(25,0), pady=(10,10), sticky='ew')

	def center_window(self, w, h):
		screen_width = self.parent.winfo_screenwidth()
		screen_height = self.parent.winfo_screenheight()

		x = int((screen_width/2) - (w/2))
		y = int((screen_height/2) - (h/2))

		centerGeo = self.parent.geometry('{}x{}+{}+{}'.format(w,h,x,y))
		return centerGeo

	def checkTime(self):
		var3 = datetime.now() - timedelta(days=1)
		return var3

	def openDir(self, var):
		dirname = filedialog.askdirectory(**self.dir_opt)
		if dirname:
			var.set(dirname)

	def sendFiles(self):
		if messagebox.askokcancel('Copy files','Do you really want to copy all {} files and paste them into folder {}?'.format(ext, self.entrytext_to.get())):
			self.folders[0] = self.entrytext_from.get()
			self.folders[1] = self.entrytext_to.get()
			check = self.checkForExistence()
			if check[0] == True:
				self.walkThruFolder(self.folders[0])
			else:
				print(check[1])
		self.var1.set('')
		self.var2.set('')

	def walkThruFolder(self, x):
		for root, dirs, files in os.walk(x):
			for f in files:
				if self.checkIfValidFile(x, f) == True:
					self.moveFiles(x, f)

	def moveFiles(self, x, f):
		pathToCheck = os.path.join(x, f)
		timeToCheck = datetime.fromtimestamp(os.path.getmtime(pathToCheck))
		minusOneDay = self.checkTime()
		if minusOneDay < timeToCheck:
			print('Files copied: ' + str(os.path.join(x, f)))
			shutil.copy(os.path.join(x, f), os.path.join(self.folders[1], f))
		else:
			print("Oustide of one day")

	def checkForExistence(self):
		if not (os.path.exists(self.folders[0]) and os.path.exists(self.folders[1])):
			return [False, 'One or both of the path names are invalid']
		else:
			return [True]

	def checkIfValidFile(self, x, f):
		if (f.endswith(ext) == True and os.path.exists(os.path.join(x, f))):
			return True
		else:
			return False


if __name__ == "__main__":
	root = Tk()
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()



		# file = Menu(menubar)
		# menubar.add_cascade(menu = file, label = 'File')
		# file.add_command(label = 'New', command = lambda: print('New file'))
		# file.add_command(label = 'Open', command = lambda: self.create_window(counter))
		# file.entryconfig('New', accelerator = 'Ctrl+N')
		# file.entryconfig('Open', accelerator = 'Ctrl+O')


		# lgth = len(self.folders)
		# num = 0
		# for f in self.folders:
		# 	print(self.folders[f])
		# 	if not os.path.exists(self.folders[f]):
		# 		print("Folder doesn\'t exist")
		# 	else:
		# 		print("good to go!")
		# 		num = num + 1
		# if (lgth == num):
		# 	print('Success')
		# else:
		# 	print('No good!!')



	# def create_window(self, counter):
	# 	counter = counter + 1
	# 	t = ttk.Toplevel(self)
	# 	t.wm_title('Window number {}'.format(counter))
	# 	l = ttk.Label(t, text='This is window #{}'.format(counter))
	# 	l.pack(side='top', fill="both", expand=True, padx=100, pady=100)
	# 	return counter


