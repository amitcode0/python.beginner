#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hi")


# # variables

# In[2]:


x=3


# In[3]:


get_ipython().run_line_magic('whos', '')


# In[4]:


print(type(x))


# In[5]:


x=3.4


# In[6]:


print(type(x))


# In[7]:


accd=4332.432


# In[8]:


get_ipython().run_line_magic('whos', '')


# In[9]:


a,b,c,d,f=2,4,6.5,6.5,-3


# In[10]:


get_ipython().run_line_magic('whos', '')


# In[12]:


del (abcd)


# In[13]:


c=3+3j


# In[14]:


print(type(c))


# # variables and operators
+ ,_, / ,% ,* ,// ,** 
# In[16]:


sumofab=a+b


# In[19]:


print(sumofab)


# In[20]:


get_ipython().run_line_magic('whos', '')


# In[21]:


sumof=a+b
print(sumof)


# In[22]:


type(a+b)


# In[24]:


v=((a+d)**3)/3


# In[27]:


print(v)


# In[28]:


s1="hello"
s2="world"
s=s1+s2
print(s)


# In[29]:


10//3


# In[30]:


10/3


# In[31]:


_


# # variable naming in python

# In[33]:


3x=5


# In[34]:


_e=6


# In[35]:


var=5


# In[36]:


DSDS=4|


# In[38]:


statingTimOFtheCourse=5


# # type of bool and comparisons
== true or flse
!=  true if not equal to

< less than
> greater then

<= less than or equal to
>= greater then or equal to

# # and or not 

# In[40]:


get_ipython().run_line_magic('whos', '')


# In[41]:


a=true
b=true


# In[42]:


a=True
b=True


# In[43]:


get_ipython().run_line_magic('whos', '')


# In[44]:


print(a and b)


# In[46]:


d=a or c
print(d)


# In[47]:


not(c)


# # camparisons
== != < > <= >=
# In[50]:


print(2<3)


# In[55]:


c=2<3
print(type(c))

print(c)


# In[59]:


d=3==4


# In[57]:


print(d)


# In[60]:


3==3.0


# In[61]:


x=4
y=9
z=8.3
r=-3


# In[62]:


(x<y) and (z<y) or (r==x)


# In[63]:


(x<y) and (r==x) or (z>y)


# In[66]:


print((not(2!=3)and True) or(False and True))


# # some useful function

# In[69]:


#rund()

print(round(45.555))


# In[76]:


#divmode()
G=divmod(34,9)


# In[78]:


type(G)
print(G)


# In[79]:


G[0]


# In[80]:


type(G)


# In[81]:


print(G)


# In[82]:


#isinstance()
print(isinstance(1,int))


# In[83]:


print(isinstance(2,float))


# In[84]:


print(isinstance(1+3j,int))


# In[86]:


#pow()
pow(3,4)


# In[87]:


pow(3,4,2)


# In[88]:


#input()
a=input("enter the number")


# In[90]:


a=float(input("enter the no:"))


# In[91]:


get_ipython().run_line_magic('pinfo', 'pow')


# In[92]:


help(input)


# # control flow

# In[100]:


a=int(input())
b=int(input())
if a>b:
    print(a)
    print("i am stilll inside if condition")
    print("i am outside")
    


# In[102]:


a=int(input())
b=int(input())
if a>b:
    print(a)
    if b>a:
        print(b)


# In[ ]:


()

