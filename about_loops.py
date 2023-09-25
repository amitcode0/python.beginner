#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=float(input("enter a real number"))
y=round(x)
if y>x:
    intportion=y-1
else:
    intportion=y
    print(intportion)


# # contro flow loops

# In[1]:


#while loop
n=int(input())
i=1
while i<n:
    print(i**2)
    print("this  is iteration number ",i)
    i+=1
    print("loop done")


# In[5]:


#even number
n=input("enter the number")
i=1
while i>n:
    if i%2==0:
        print(i)
        else
            i+=
            continue
            print("i am inside the loop")
            print("done")


# In[6]:


n=10
i=1
while True:
    if i%0==0:
        print("")
        break
        else:
            i=i+1
            print("done")


# # for loop

# In[12]:


L=[]
for i in range (0,10,2):
    print(i)
    L.append(i**2)
    print(L)


# In[13]:


S={"HI",5.6,"HO"}
for x in S:
    print(x)
    i
    else:
        print("loop")
        print("out")


# In[15]:


d={"apple":44,"hi":70}
for x in d:
    print(x,d[x])


# In[19]:


#problem
"""given a list of a numbers i.e [1,2,3,-5,6,8,9] ,making another 
list that cantains all the items in order from min to max i.e
ypur result will be another list lik  [-4,5,7,4,3,3,5]"""


L=[1,2,3,-4,6,8,9]
m=L[0]
idx=0
c=0
for i in L:
    if i<m:
        m=i
        idx=c
        c+=1
        print(idx,m)


# In[ ]:





# # 
# # functions

# In[26]:


def hi():
    print("i am ok")
    print("send me another task")


# In[27]:


hi()


# # doc string

# In[33]:


def h2():
    """this code will just print the message"""
    
    print("hello")
    


# In[30]:


hi


# In[31]:


h2


# In[32]:


h2()


# In[35]:


get_ipython().run_line_magic('pinfo2', 'h2')


# In[36]:


get_ipython().run_line_magic('pinfo', 'len')


# In[37]:


help(hi)


# In[38]:


hi()


# In[ ]:




