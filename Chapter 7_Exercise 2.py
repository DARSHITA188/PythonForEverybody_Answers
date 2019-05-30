#!/usr/bin/env python
# coding: utf-8

# In[1]:


count = 0
sum=0

fname = input("enter file name: ")
try:
    fhand = open(fname) 
    for line in fhand: 
        if line.startswith('X-DSPAM-Confidence:'): 
            apos = line.find(':')
            bpos = line.find('.',apos)
            substr=line[apos+2:bpos+5]
            substr = float(substr)
            sum = sum+substr
            count = count+1
    print("average X-DSPAM-Confidence: ", sum/count)
    
except:
    print("file doesn't exists")


        
        


# In[ ]:





# In[ ]:




