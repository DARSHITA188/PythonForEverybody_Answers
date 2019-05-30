#!/usr/bin/env python
# coding: utf-8

# In[3]:


total = 0
count = 0
average = 0

while True:
  try:
    x = input("Enter a number: ")
    if (x == "done"): 
     break
    value = float(x)
    total = total + value
    count = count + 1
    average = total / count
  except:
    print("Invalid input.")
print("total",total,"count",count,"average",average)


# In[ ]:




