### This program moves all text files from one folder to another.
### Uncomment to execute

# import os
# cwd = os.getcwd()
# count = 0

# for root, dirs, files in os.walk(cwd):
	
# 	newFolder = cwd + '/newTextFiles'
# 	if not os.path.exists(newFolder):
# 		os.makedirs(newFolder)
	
# 	for f in files:
# 		oldPath = os.path.join(cwd, f)
# 		if f.endswith('.txt'):
# 			if os.path.exists(oldPath):
# 				newPath = os.path.join(newFolder, f)
# 				os.rename(oldPath, newPath)
# 				print('The file ' + newPath + ' was moved')
# 				count = count + 1

# 	if not (count > 0):
# 		print('My goodness! You have no text files in this folder!')
# 		break