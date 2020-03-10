#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 09:47:36 2020

@author: hannahmacdonell
"""

#N: Musical Instruments(itemID, instrType)

import random
import csv

l = []
c = open("InstrType.txt", "r")
for line in c:
    l.append(line.strip().split('\n')[0])
    
with open('instrument.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',')
    data_writer.writerow(['InstrType'])
    for x in range(1000):
        data_writer.writerow([l[random.randint(0,len(l)-1)]])
        
data_file.close()

