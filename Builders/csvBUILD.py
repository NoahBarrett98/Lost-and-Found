#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:26:43 2020

@author: hannahmacdonell
"""
import random 
import csv

a = []
import string
letters = list(string.ascii_lowercase)
letters.extend([i+b+c for i in letters for b in letters for c in letters])
letters = letters[26:]
years = ['2014','2015','2016','2017','2018','2019','2020']
for x in letters:
    a.append('x'+years[random.randint(0,len(years)-1)]+x)


b = []
outF = open("first_names.txt", "r")
for line in outF:
    b.append(line.strip().split('\n')[0])
outF.close()


c = []
outF = open("lastName.txt", "r")
for line in outF:
    c.append(line.strip().split('\n')[0])
outF.close()


d = []
outF = open("adress.txt", "r")
for line in outF:
    d.append(line.strip().split('\n')[0])
outF.close()


with open('data_file.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',')
    data_writer.writerow(['userID','fName','lName','userAddress'])
    i=0
    while(i<1000):
        data_writer.writerow([a[i],b[random.randint(0,len(b)-1)],c[random.randint(0,len(c)-1)],d[random.randint(0,len(d)-1)]])
        i = i+1
        
data_file.close()
            
#H:User(userID, firstName, lastName, userAddress) 