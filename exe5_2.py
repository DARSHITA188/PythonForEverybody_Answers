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


# In[6]:


count = 0
total = 0
avg = 0
largest = None
smallest = None
keepgoing = True
while keepgoing:
  prompt1 = 'Enter a number \n'
  line = input (prompt1)
  try:
     line = float(line)
     count = count + 1 
     total = total + line
     avg = total / count
     if smallest is None or line < smallest:
      smallest = line
     if largest is None or line > largest:
      largest = line
  except:
    if line == 'Done' or line == 'done':
      break
    else:
      print('Invalid Input')
      continue
print("count",count,"largest",largest,"smallest",smallest)

