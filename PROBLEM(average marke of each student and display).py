#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""let say you are a teacher and you have different 
student records cantaining id of a student and the marke 
list in each subject where different students have taken 
different number of subjects.All these records ar in hard
copy. You want to enter all the data in computer and want 
to compute the average marke of each student and display
"""


# In[13]:


def get_data_from_user():
       D={}
       while True:
           studentID=input("enter student ID:")
           marklist=input("enter the marks by commo seprated values:")
           morestudent=input("enter yes/no for adding more student:")
           if studentID in D:
               print(studentID,"is alreday insterted")
           else:
                   D[studentID]=marklist.split(",")
                   if morestudent.lower()=="no":
                       return D


# In[ ]:


studentData=get_data_from_user()


# In[ ]:


def getavgmark(D):
    avgmarks={}
    for x in D:
        l=D[x]
        s=0
        for marks in l:
            s+=int (marks)
            getavgmark[x]=s/len(l)
            return avgmarks


# In[ ]:


avgm=getavgmark(studentData)


# 

# In[ ]:


for x in avgm:
    print("student:",x,"got avg marks as :",avgm[x])


# In[ ]:




