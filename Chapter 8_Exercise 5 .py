#!/usr/bin/env python
# coding: utf-8

# In[1]:


count = 0
fname = input("enter file name: ")
try:
    fhand = open(fname) 
    for line in fhand: 
        if line.startswith('From '):
            words = line.split(" ")
            print(words[1])
            count = count+1;
    print("Total email sender : ", count)
except:
    print("file not")


# In[ ]:





# In[ ]:




