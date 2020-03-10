#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:28:06 2018

@author: hannahmacdonell
"""


"1. Takes file in 'Abcdefgh,ABCD' format and makes it ABCD"
"*** IndecError Version rn***"

l=[]
outF = open("UsedIn.txt", "r")
for line in outF:
    line=line.split(',')
    try:
        l.append(line[1])
    except IndexError:
        l.append(' \n')
outF.close()

outF = open("ISBN.txt", "w")
for i in l:
    outF.write(i+'\n')
outF.close()


"2. Addess fixer upper"
l=[]
addy = open("adress.txt","r")
for line in addy:
    l.append(line)
addy.close()
new = open("adress.txt","w")
i = 0
j = 1
m=[]
while(j<len(l)):
    print(l[i].strip().split('\n')[0]+l[j].strip().split('\n')[0])
    new.write(str(l[i].strip().split('\n')[0]+l[j]))
    i=i+2
    j=j+2
new.close()

"3. Building student ID's"

import string
letters = list(string.ascii_lowercase)
letters.extend([i+b+c for i in letters for b in letters for c in letters])
letters = letters[26:]
print(letters)


"4. Making course file make more sense"

import random
years = ['2014','2015','2016','2017','2018','2019','2020']
l=[]

outF = open("courses.txt", "r")
for line in outF:
    l.append(line.strip().split('\n')[0] + ','+
             str(years[random.randint(0,3)]) + ','+
             str(random.randint(1000,5000)) + '\n')
    
    l.append(str(line.strip().split('\n')[0]) + ',' +
             str(years[random.randint(4,6)]) + ',' +
             str(random.randint(1000,5000)) + '\n') 
outF.close()

outF = open("courses.txt", "w")
for i in l:
    outF.write(i)
outF.close()








    

            
            
            
            


