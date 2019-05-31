#!/usr/bin/env python
# coding: utf-8

# In[4]:


import string

count = 0

count = 0                          
dictionary = dict()
var = list()
file_name = input('File name is: ')

try:
    fhand = open(file_name)
    
except FileNotFoundError:
    print('Error. File not found, Please enter valid name', file_name)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    
    for word in words:
        for letter in word:
            
            count += 1
            
            if letter not in dictionary:
                dictionary[letter] = 1
            
            else:
                dictionary[letter] += 1

for key, val in list(dictionary.items()):
    var.append((val / count, key))

var.sort(reverse=True)

for key, val in var:
    print(key, val)


# In[ ]:




