#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11. Converting a List into a String


# In[4]:


list=["hi",'my','is ','amit']
string="".join(list)
print(string)
print(type(string))


# In[5]:


#12. Adding Two List Elements Together


# In[ ]:





# In[ ]:





# In[2]:


list1=[2,3,2]
list2=[2,3,3]
newlist=[]
for i in range(0,len(list1)):
    newlist.append(list1[i]+list2[i])
    print(newlist)


# In[14]:


#13. Comparing Two Strings for Anagrams
str1 = "how"
str2 = "hi"

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort(), str2.sort()

if(str1 == str2):
    print("True")
else:
    print("False")


# In[ ]:


#14. Checking for Palindrome Using Extended Slicing Technique


# In[24]:


str1="hi".lower()n
str2="hhii".lower()

if(str1==str2[::-1]):
    print("true")
else:
    print("false")


# In[ ]:


#15. Counting the White Spaces in a String


# In[25]:


st="how are you man"
print(st.count(""))


# In[26]:


#16. Counting Digits, Letters, and Spaces in a String


# In[ ]:





# In[33]:


import re

name = 'i am 1'

digit= re.sub("[^0-9]", "", name)
letter = re.sub("[^a-zA-Z]", "", name)
space = re.findall("[ \n]", name)

print(len(digit))
print(len(letter))
print(len(space))


# In[34]:


#17. Counting Special Characters in a String


# In[43]:


import re
Char = "!@%^&()"

count = re.sub('[\w]+', '', Char)
print(len(count))
    


# In[44]:


#18. Removing All Whitespace in a String


# In[46]:


import re
string='a b cdf '
space=re.compile(r'\s+')
result=re.sub(space,'',string)
print(result)


# In[47]:


#19. Building a Pyramid in Python


# In[53]:


p = 10
h = 2*floors-1
for i in range(1, 2*p, 2):
    print('{:^{}}'.format('*'*i, h))


# In[ ]:


#20. Randomizing the Items of a List in Python


# In[55]:


from random import shuffle

lst = ['i ', 'am', 'good']
shuffle(lst)
print(lst)


# In[ ]:




