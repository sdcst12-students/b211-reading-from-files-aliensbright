"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math

filename2a = 'task02a.txt'
file2a = open(filename2a,'r')
data2a = file2a.read()

filename2b = 'task02b.txt'
file2b = open(filename2b,'r')
data2b = file2b.read()

filename2c = 'task02c.txt'
file2c = open(filename2c,'r')
data2c = file2c.read()


def sortFile(file):
    Mylist=file.split('\n')
    Mylist = list(filter(None,Mylist))
    return Mylist

def sortTriples(list):
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
                assert a == (b**2 + c**2)**0.5
                numoftriples = numoftriples + 1
            except:
                pass
        elif x==b:
            try:
                assert b == (a**2 + c**2)**0.5
                numoftriples= numoftriples + 1
            except:
                pass
        elif x==c:
            try:
                assert c == (b**2 + a**2)**0.5
                numoftriples = numoftriples + 1
            except:
                pass
    return(numoftriples)


list2a = sortFile(data2a)
triples2a = sortTriples(list2a)
numTrip2a = checkTriples(triples2a)

list2b = sortFile(data2b)
triples2b = sortTriples(list2b)
numTrip2b = checkTriples(triples2b)

list2c = sortFile(data2c)
triples2c = sortTriples(list2c)
numTrip2c = checkTriples(triples2c)

print(f"The triples contained are [2a ; {numTrip2a}, 2b ; {numTrip2b}, 2c ; {numTrip2c}]")