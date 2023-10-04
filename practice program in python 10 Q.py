#!/usr/bin/env python
# coding: utf-8

# # practice program in python 10 Q

# In[1]:


#1. Converting an Integer into Decimals


# In[2]:


import decimal
int=30
print(decimal.Decimal(int))
print(type(decimal.Decimal(int)))


# In[3]:


#2. Converting an String of Integers into Decimals


# In[8]:


import decimal
str="13332323"
print(decimal.Decimal(str))
print(type(decimal.Decimal(str)))


# In[9]:


#3. Reversing a String using an Extended Slicing Technique


# In[14]:


str_1="i am good "
print(str_1[::-1])


# In[15]:


#4. Counting Vowels in a Given Word


# In[20]:


vowels=['a','e','i','o','u']
cout_in_word="i am good now"
cout=0
for char in cout_in_word:
    if char in vowels:
        cout+=1

        print(cout)


# In[ ]:


#5. Counting Consonants in a Given Word


# In[24]:


v=['a','e','i','o','u']
in_word="bcaaaad"
cout=0
for chr in in_word:
    if chr not in v:
        cout+=1
        print(cout)


# In[1]:


#6. Counting the Number of Occurances of a Character in a String


# In[6]:


word='i am good'
char="a"
count=0
for letter in word :
    if letter ==char:
        count+=1
        print(count)


# In[7]:


#7. Writing Fibonacci Series


# In[12]:


fib=[0,1]
for i in range (2):
    fib.append(fib[-1]+fib[-2])
    print(','.join(str(e)for e in fib))


# In[14]:


#8. Finding the Maximum Number in a List


# In[17]:


list1=[2,4,5,2,1,4,420]
maxnum=list1[0]
for num in list1:
    if maxnum<num:
        maxnum=num
        print(maxnum)


# In[18]:


# 9. Finding the Minimum Number in a List


# In[27]:


list1=[22,41,5,22,11,4,420]
min1=list1[0]
for num in list1:
    if min1>num:
        min1=num
        print(min1)


# In[28]:


#10. Finding the Middle Element in a List



# In[32]:


list1=[2,4,4,2,4,323,223]
midd=(int(len(list1)/2))
print(list1[midd])


# In[ ]:




