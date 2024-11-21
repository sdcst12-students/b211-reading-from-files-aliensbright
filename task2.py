"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math

filename = 'task02a.txt'
file = open(filename,'r')
data = file.read()


def sortFile(file):
    Mylist=file.split('\n')
    Mylist = list(filter(None,Mylist))
    return Mylist

def SortTriples(list):
    SortedList = []
    print(list)
    a = int(len(list)/3)
    for i in range(a):
        x = int(list[i*3]) , int(list[i*3+1]) , int(list[i*3+2])
        SortedList.append(x)
    return SortedList

def checkTriples(listinlist):
    numoftriples = 0
    for i in listinlist:
        a = i[0]
        b = i[1]
        c = i[2]
        x = max(a,b,c)
        if x==a:
            try:
                assert a == (b^2 + c^2)^0.5
                numoftriples = numoftriples + 1
            except:
                pass
        elif x==b:
            try:
                assert b == (a^2 + c^2)^0.5
                numoftriples= numoftriples + 1
            except:
                pass
        elif x==c:
            try:
                assert c == (b^2 + a^2)^0.5
                numoftriples = numoftriples + 1
            except:
                pass
    return(numoftriples)


        


AllVals = sortFile(data)

hi = SortTriples(AllVals)

hello = checkTriples(hi)

print(hello)