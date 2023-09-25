#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:18:43 2022

@author: amitprajapati
"""

#amit prajapati

#Accepting the values
n=input('Enter users name : ')
t=n


#1st problem

print('name in lower case : ',n.lower())
n.upper()
print('name in upper case : ',n.upper())

#2nd problem
print('Length of the name : ',len(n))

#3rd problem
countr=0
for i in range (0,len(t),1):
    if(t[i]=='R' or t[i]=='r'):
        countr+=1
    else:
        continue
if(countr>0):
    print('R/r is present in the name ')
else:
    print('R/r is not present in the name ')
        
#4th problem
counta=0
for i in range (0,len(t),1):
    if(t[i]=='A' or t[i]=='a'):
        counta+=1
    else:
        continue

if(counta>0):
    print('A/a is present in the name ')
else:
    print('A/a is not present in the name ')
