# -*- coding: utf-8 -*-
"""
file io workspace


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

text = open("Textbook.txt", "r")
write = open("Textbook.dat", "w")
for line in text.readlines():
    write.write(line[:-3]+ '\n')
write.close()
text.close()