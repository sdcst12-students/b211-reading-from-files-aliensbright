#!python3
# Advanced Dungeons and Dragons

"""
the file task04.txt contains a matrix of values
The row indicates the level of fighter. Row 1 is for a level 1 fighter, row 2 is for a level 2 fighter and so on

In each row, the numers indicate the target number needed out of 20 to land a hit on a specific Armor Class, starting with
10 on the left, followed by 9, then 8, all the way to -10 on the far right.

Create a function that reads the specific value for a specific level and an armor class, and prints the target number needed.

#10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10 
 10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 22 23 24 25 #1
 10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 22 23 24 25 #2
 9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 22 23 24 #3
 9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 22 23 24 #4
 8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 22 23 #5
 8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 22 23 #6
 7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 22 #7
 7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 22 #8
 6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 #9
 6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 21 #10
 5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 #11
 5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 20 #12
 4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 #13
 4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 20 #14
 3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 #15
 3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 20 #16
 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 #17
 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 20 20 #18



"""
filename4 = 'task04.txt'
file4 = open(filename4,'r')
data4 = file4.read()

data4=data4.split("\n")
global table
table=[]
lines=[]
for i in data4:
    i=i.split(" ")
    lines=[]
    for a in i:
        lines.append(a)
    table.append(lines)



def target(lvl,ac):
    m = table[lvl-1]
    ac = 10 - ac
    m = m[ac]
    m=int(m)
    return m


def tests():
    #assert target(3,7) == 23
    assert target(3,7) == 12
    assert target(3,-9) == 23
    assert target(9,-1) == 17
    assert target(13,-10) == 20
    print('done')

if __name__=="__main__":
    tests()