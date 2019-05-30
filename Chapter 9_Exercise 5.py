#!/usr/bin/env python
# coding: utf-8

# In[1]:


count = 0
d = dict() 
fname = input("enter file name: ")
try:
    fhand = open(fname) 
    for line in fhand: 
        if line.startswith('From '):
            words = line.split(" ")
            string = words[1]
            apos = string.find('@')
            substr = string[apos+1:]
            if substr not in d: 
                d[substr] = 1 
            else: 
                d[substr] = d[substr] + 1
    
    print("Dictionary content: ",d)
except:
    print("file not there")


# In[ ]:




