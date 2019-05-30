#!/usr/bin/env python
# coding: utf-8

# In[1]:


list0 = []
list1 = []
list2 = []
list3 = []
mainList = []
file = input("Enter file: ")
fhand = open(file)
lines = fhand.read()
for line in lines:
    line = lines.split('\n')
    for word in line[0]:
        list0 = line[0].split(' ')
    for word in line[1]:
        list1 = line[1].split(' ')
    for word in line[2]:
        list2 = line[2].split(' ')
    for word in line[3]:
        list3 = line[3].split(' ')
mainList = list0+list1+list2+list3;
mainList = sorted(mainList)
print(mainList)
    


# In[ ]:





# In[ ]:




