#!/usr/bin/env python3
import glob
import fileinput

def crawl():
	for fn in glob.glob('*.cpp'):
		fileName = fn.split('.')[0]
		functionToReplace = 'int main('
		newFunctionDef = 'int '+ fileName +'('
		headerFileName = fileName + '.h'
		repStatus = False
		# include header 
		with open(fn, 'r+') as file:
			content = file.read()
			file.seek(0)
			include = '#include '+'"'+headerFileName+'"'
			if not(include in content):
				file.write(include + '\n\n'+content)
		# replace function definition
		res = None
		with open(fn, 'r+') as file:
			for line in file:
				line = line.rstrip()
				if functionToReplace in line:
					res = line.replace(functionToReplace, newFunctionDef)
		print(res)
		with fileinput.FileInput(fn, inplace=True) as file:
			for line in file:
				if functionToReplace in line:
					repStatus = True
				print(line.replace(functionToReplace, newFunctionDef), end='')
#				print(line.strip())
#
#		print(result)
		# create header file
		if res:
			with open(headerFileName, 'w+') as headerFile:
				headerFile.write(str(res)+';');
		# return status
		print(fn + ' ' + str(repStatus))
