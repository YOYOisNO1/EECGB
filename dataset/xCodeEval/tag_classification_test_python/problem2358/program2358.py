def program2358():
    import sys
    n,m,a,b=map(int,input().split())
    if(n%m==0):
        print("0")
    elif(n>m):
        count=n%m
        mul=((m-count)*a)
        d=(count*b)
        if(mul<d):
            print(mul)
        else:
            print(d)
    elif(n<m):
        count=(m-n)*a
        count1=n*b
        if(count>count1):
            print(count1)
        else:
            print(count)