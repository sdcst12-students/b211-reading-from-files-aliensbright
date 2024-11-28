#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""


filename3 = 'task03.txt'
file3 = open(filename3,'r')
data3 = file3.read()

listofsums = []
global indexofspaces
indexofspaces = []

def listsofvals(file): #def find_positions(lst, value): return [index for index, element in enumerate(lst) if element == value]
    Mylist=file.split('\n')
    count = -1
    for i in Mylist:
        count+=1
        if i =='':
            indexofspaces.append(count)
    print("index of spaces",indexofspaces)
    return indexofspaces
    


def sumofvals(list,val1,val2):
    print(list)
    print('val1=',val1,'val2',val2)
    newlist=list[val1:val2]
    print('newlist',newlist)
    sum=0
    for i in newlist:
        sum=i+sum
    print("sum=",sum)
    return sum



sorted3 = listsofvals(data3)

for num in range(len(sorted3)):
    n = sumofvals(data3,sorted3[num],sorted3[num+1])
    listofsums.append(n)
    #print(listofsums)

maxSum = max(listofsums)

print(f"For sample data task03.txt, the largest sum should be {maxSum}")
