#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:28:50 2020

@author: hannahmacdonell
"""
l=[]
outF = open("Abbrevs.txt", "r")
for line in outF:
    l.append(line.strip().split('\n')[0])

    

g = []
s=[]
i = 0
for x in l:
    if x in s: 
        g.append(x) 
        print(l[i-1])
        i = i + 1
    s.append(x)
    i = i + 1

print(l)
print("\n ------ \n")
print(g)

outF.close()
