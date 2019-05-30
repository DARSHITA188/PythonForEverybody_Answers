#!/usr/bin/env python
# coding: utf-8

# In[11]:


str = 'X-DSPAM-Confidence:0.8475'
apos = str.find(':')
bpos = str.find('5',apos)
substr=str[apos+1:bpos+1]
substr = float(substr)
print("Substring: ", substr)
print("Type: ", type(substr))


# In[ ]:




