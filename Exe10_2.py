#This program counts the distribution of the hour of the day for each of
#the messages.You can pull the hour from the “From” line by ﬁnding the
#time string and then splitting that string into parts using the colon
#character.

import string
file_name = input('File name is: ')

try:
	fhandle = open(file_name)
except:
	print ('File cannot be opened:', file_name)
	exit()

letters = dict()
for line in fhandle:
	line = line.translate(string.punctuation)
	line = line.translate(string.digits)
	line = line.lower()
	line = line.split()
	for t in line:
		word = list(t)
		for letter in word:
			letters[letter] = letters.get(letter,0) + 1

letterlist = []
for letter, count in letters.items():
	letterlist.append( (count, letter) )
letterlist.sort(reverse=True)
for count, letter in letterlist:
	print (letter, count)
