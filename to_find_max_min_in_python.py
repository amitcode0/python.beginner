#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:20:42 2022

@author: amitprajapati
"""
#by amit prajapati

n1=int(input('Enter a num : '))
n2=int(input('Enter a num : '))
n3=int(input('Enter a num : '))
n4=int(input('Enter a num : '))
lst=[]
lst.append(n1)
lst.append(n2)
lst.append(n3)
lst.append(n4)

#Max Number
if(n1>n2):
    if(n1>n3):
        if(n1>n4):
            print('Max number is ',n1)
        else:
            print('max number is ',n4)
    elif(n3>n4):    
        print('Max number is ',n3)
    else:
        print('Max number is ',n4)
elif(n2>n3):
    if(n2>n4):
        print('max number is ',n2)
    else:
        print('max number is ',n4)
elif(n3>n4):
    print('Max number is ',n3)
else:
    print('Max number is ',n4)

#Min Number
if(n1<n2):
    if(n1<n3):
        if(n1<n4):
            print('Min number is ',n1)
        else:
            print('Min number is ',n4)
    elif(n3<n4):    
        print('Min number is ',n3)
    else:
        print('Min number is ',n4)
elif(n2<n3):
    if(n2<n4):
        print('min number is ',n2)
    else:
        print('min number is ',n4)
elif(n3<n4):
    print('Min number is ',n3)
else:
    print('Min number is ',n4)
