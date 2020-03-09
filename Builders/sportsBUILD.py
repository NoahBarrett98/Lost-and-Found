#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 09:52:04 2020

@author: hannahmacdonell
"""

#H: Sporting Goods(itemID, sport)


import random
import csv

l = []
c = open("sports.txt", "r")
for line in c:
    l.append(line.strip().split('\n')[0])
c.close()
    
with open('sports.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',')
    data_writer.writerow(['Sport'])
    for x in range(1000):
        data_writer.writerow([l[random.randint(0,len(l)-1)]])
        
data_file.close()
