    import os
def readInts(): return map(str,input().split())
    n=readInts()[0]
    n1=n
    n1='.'.join(n1)
    n1=n1.split(".")
    temp=n
    flag=True
    c=1
    while flag:
        temp=str(int(temp)+c)
        temp='.'.join(temp)
        temp=temp.split(".")
        test=list(set(temp))
        temp2=""
        for i in temp:
            temp2=temp2+i
        c=len(test)
        temp=temp2
        if c ==len(n):
            flag=False
            #temp=temp2
        if c>2:
            c=c//2
    print(temp)