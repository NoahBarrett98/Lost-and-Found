#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 09:42:47 2020

@author: hannahmacdonell
"""

#T: Clothing(itemID, cBrand, size, article)


import random
import csv


d = []
c = open("cBrand.txt", "r")
for line in c:
    d.append(line.strip().split('\n')[0])
c.close()
    

l = []
c = open("size.txt", "r")
for line in c:
    l.append(line.strip().split('\n')[0])
c.close()
    
a = []
c = open("article.txt", "r")
for line in c:
    a.append(line.strip().split('\n')[0])
c.close()

with open('clothing.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',')
    data_writer.writerow(['CBrand','Size','Article'])
    for x in range(1000):
        data_writer.writerow([l[random.randint(0,len(l)-1)],d[random.randint(0,len(d)-1)],a[random.randint(0,len(a)-1)]])
        
data_file.close()
