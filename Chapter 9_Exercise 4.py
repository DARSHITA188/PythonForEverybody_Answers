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
            
            
            if words[1] not in d: 
                d[words[1]] = 1 
            else: 
                d[words[1]] = d[words[1]] + 1 
    
    #print(d)
    largest = None 
    for key in d: 
        if largest is None or d[key] > largest : 
            largest = d[key] 
             
    
    print("Sender with most messages: ", key)
    print("count: ", largest)
    

                  
except:
    print("file not") 




# In[ ]:





# In[ ]:




