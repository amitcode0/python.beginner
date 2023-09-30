#!/usr/bin/env python
# coding: utf-8

# # Numpy

# In[1]:


import numpy as np


# In[4]:


a=np.array([1,2,3,3,3,])
b=np.array((1,2,3,4,4,4))
print(a)
print(b)


# In[6]:


type(b)


# In[7]:


a.dtype


# # Numpy(Dimensions) type dtype ndim

# In[15]:


#2D array
a=np.array([[1,2,2,2],[1,32,3,5]])
print(a)
print(a.ndim)


# In[16]:


a[0,2]


# In[27]:


c=np.array([[1,1,2,3,3],[22,4,32,3]])
print(c)
print(c.ndim)


# In[32]:


arr= np.array([[[1, 2, 3], [4, 7, 0]], [[1, 10, 9], [10, 11, 12]]])


# In[33]:


print(arr)


# In[34]:


type(arr)


# In[37]:


a.shape[1]


# In[38]:


type(c)


# In[39]:


A=np.array([1])


# In[40]:


A.ndim


# In[41]:


b.ndim


# In[43]:


a.size


# # Numpy(np.arrange, reshape, random)

# In[48]:


a=np.arange(27)
print(a)


# In[49]:


a=np.arange(27,100)
print(a)


# In[50]:


a=np.arange(27,100,3)
print(a)


# In[53]:


print(range(20))


# In[55]:


print(list(range(10)))


# In[62]:


D= np.random. permutation(np.arange(20)) 


# In[63]:


print(D)


# In[65]:


np.random.randint(10,20) #random number 


# In[74]:


c=np.random.rand(100)


# In[69]:


import matplotlib.pyplot as plt


# In[78]:


plt.hist(a,bins=17)


# In[79]:


b=np.random.rand(100000)


# In[85]:


plt.hist(b,bins=200)


# 

# In[91]:


m=np.random.rand(2,3)
print(m)


# In[92]:


m.ndim


# In[93]:


m=np.random.rand(2,3,3,4)
print(m)


# In[94]:


m.ndim


# In[96]:


D = np. arange (100) .reshape (4,25)


# In[98]:


D.shape


# In[111]:


D = np.arange (100) . reshape (4,5,5)


# In[104]:


D.shape


# In[105]:


get_ipython().run_line_magic('pinfo', 'np.zeros')


# In[106]:


get_ipython().run_line_magic('pinfo', 'np.ones')


# # Numpy(Slicing)

# In[112]:


a=np.arange(100)


# In[114]:


b=a[4:5]
print(b)


# In[115]:


b[0]=19


# In[116]:


b


# In[117]:


a


# In[119]:


b=a[4:15].copy()


# In[120]:


b


# In[121]:


a[::4]


# In[124]:


b[::-4]


# In[126]:


a[::-1]


# In[132]:


b= (a==-1200) *np.arange (a.size)


# In[134]:


a


# In[139]:


idx = np.argwhere (a==19)[0][0]


# In[140]:


idx


# In[164]:


a=np.round(10*np.random.rand(4,4)


# In[169]:


a


# In[166]:


import numpy.linalg as la


# In[167]:


la.inv(np.random.rand(3,3))


# In[3]:


a.sort(axis=1)


# # Numpy(More Indexing)

# In[5]:


import numpy as np


# In[9]:


a=np.arange(100)


# In[10]:


b=a[[1,2,32,3]]


# In[11]:


b


# In[14]:


b[0]=-4


# In[15]:


b


# In[16]:


a


# In[17]:


b=a[a<40]


# In[18]:


b


# In[24]:


b=a[(a<40)&(a>20)]


# In[22]:


b


# # Numpy (Broadcasting)

# In[25]:


a=np.random.rand(2,3)


# In[26]:


a


# In[27]:


a+3


# In[28]:


a+(np.arange(2).reshape(2,1))


# In[29]:


a


# In[30]:


b=np.round(10*np.random.rand(2,2))


# In[31]:


b


# In[32]:


c=np.hstack((a,b))


# In[33]:


c


# In[34]:


a=np.random.permutation(np.arange(10))


# In[35]:


a


# In[37]:


a.sort()


# In[38]:


a


# In[44]:


a.sort()


# In[40]:


a=a[::-1]


# In[41]:


a


# In[43]:


a=np.array(["abc",'how are'])


# In[45]:


a.sort()


# In[46]:


a


# In[49]:


b=np.random.rand(1000000)
get_ipython().run_line_magic('timeit', 'sum(b)')
get_ipython().run_line_magic('timeit', 'np.sum(b)')


# In[ ]:




