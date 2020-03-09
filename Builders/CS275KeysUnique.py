#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:44:37 2020

@author: hannahmacdonell
"""

abr = []
fp = open('Abbrevs.txt', 'r')
for line in fp:
    line.replace('\\', "")    
    l = line.split(',')
    print (l[1])
    abr.append(l[1])


