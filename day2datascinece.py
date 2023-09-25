#!/usr/bin/env python
# coding: utf-8

# # a=1
# b=5
# if a==b:
#     print("equal")
#     elif a>b:
#         print("A")
#         else:
#             print("B")
#         print("not in if")

# In[7]:


a=int(input("enter a mark"))
if a >=85:
     print("A grade")
elif a < 85 and a>=80:
    print("A- grade")
elif a<80 and a>=75:
    print("B grade")
elif a<75 and a>=70:
    print("B- grade")
else:
    print("below average")


# In[8]:


a=3
if a>10:
    print(">10")
elif not(a>10):
    print("else part")


# # nested if

# In[12]:


x=int(input("enter a num"))
if x>10:
    print("your number above 10")
    print("inside the top if")
    if a>20:
        print(">20")
        print("inside the nested if")
    else:
        print("<=20")
        print("inside the else part of nested if")
print("oute side all ifs")


# In[ ]:




