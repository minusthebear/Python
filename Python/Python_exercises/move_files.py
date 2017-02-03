import os
from datetime import datetime, timedelta

fmt = '%Y-%m-%d %H:%M:%S'
timeNow = datetime.now().strftime(fmt)
minusOneDay = datetime.now() - timedelta(days=1)
print(timeNow)
print(minusOneDay)

folders = ('/old_folder1', '/new_folder2')
filesToWrite = ('file1.txt', 'file2.txt', 'file3.txt', 'file4.txt')

for f in folders:
	link = os.getcwd() + f
	if not os.path.exists(link):
		try:
			os.makedirs(link)
		except OSError:
			print('Sorry, I can\'t perform the operation')

r_f = os.getcwd() + folders[0]
n_f = os.getcwd() + folders[1]

for root, dirs, files in os.walk(r_f):
	if (len(files) <= 0):
		for f in filesToWrite:
			with open(os.path.join(r_f, f), 'w+') as w:
				w.write(str(f) + ' is the name of the file')

for root, dirs, files in os.walk(r_f):
	for f in files:
		pathToCheck = os.path.join(r_f, f)
		time = datetime.fromtimestamp(os.path.getmtime(pathToCheck)).strftime(fmt)
		timeMinusOne = datetime.fromtimestamp(os.path.getmtime(pathToCheck)) - timedelta(days=1)
		if minusOneDay <= timeMinusOne:
			os.rename(pathToCheck, os.path.join(n_f, f))
			print('Files moved: ' + str(os.path.join(n_f, f)))
		else:
			print('Files NOT moved: '+ str(pathToCheck))