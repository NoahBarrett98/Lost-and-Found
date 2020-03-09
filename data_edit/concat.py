# -*- coding: utf-8 -*-
"""
file io workspace
"""
"""
#making crns same
Class = open('class.txt', "r")
Isbn = open('Isbn.txt', "r")
Usedin = open('UsedIn.txt', "r")
UsedInNew =  open('UsedInNew.txt', "w")
CRN_ISBN = []
for i, j in zip(Class.readlines(),Isbn.readlines()):
    i = i.split(',')
    j = j.split(',')
    CRN_ISBN.append([i[0], j[0]])

    
for i, l in enumerate(Usedin.readlines()):
    l = l.split(',')
    l[0] = CRN_ISBN[i][0]
    l[1] = CRN_ISBN[i][1]
    s = ''
    for i in l:
        s+=i +','
    s = s[:-1]
    UsedInNew.write(s)
    

         
Class.close()
Isbn.close()
Usedin.close()
UsedInNew.close()
"""
"""
text = open("Inventory.txt", "r")
write = open("Inventory.dat", "w")
for line in text.readlines():
    line = line.split(',')
    line[0] = "000" + line[0]
    s = ''
    for n in line:
        s += n +','
    write.write(s[:-1]+ '\n')
write.close()
text.close()
"""
"""
format dates
"""
"""

text = open("Inventory.txt", "r")
dates = open("dates.txt", "r")
dates = dates.readlines()
write = open("Inventory.dat", "w")
for i, line in enumerate(text.readlines()):
    line = line.split(',')
    line[3] = dates[i%1000][:-1]
    s = ''
    for n in line:
        s += n +','
    write.write(s[:-1])
write.close()
text.close()
"""

"""
text = open("Inventory.txt", "r")
write = open("Inventory.dat", "w")
for line in text.readlines():
    line = line.split(',')
    if line[2][0] == "$":
        line[2] = line[2][1:]
    s = ''
    for n in line:
        s += n +','
    write.write(s[:-1])
write.close()
text.close()
"""