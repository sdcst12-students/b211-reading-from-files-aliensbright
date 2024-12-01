"""
Read the data from the file task5.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

filename5 = 'task5.csv'
file5 = open(filename5,'r')
data5 = file5.read()


data5=data5.split("\n")
newlist=[]

for i in data5:
    x=i.split(',',1)
    newlist.append(x)

def numVals(string):
    count=0
    comp=''
    for i in newlist:
        x=i[0]
        try:
            assert string in x
            count += 1
            if string==x:
                count=1
                comp=i[1]
                break
        except:
            pass

    return count, comp

while True:
    sym = input("Enter stock symbol: ")
    occur,company = numVals(sym)
    if occur==0:
        print("No match found")
    elif occur==1:
        print(company)
    else:
        print(f"There are {occur} stocks with that symbol")


