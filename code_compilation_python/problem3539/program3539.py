    import math
    a,b = map(int,input().split())
def lcm(a,b):
        if(a>b):
            min1=a
        else:
            min1=b
        while(1):
            if(min1%a==0 and min1%b==0):
                return(min1)
            min1=min1+1
    min1 =lcm(a,b)
    k=0
    num = abs(a-b)
    if num >=10**4 :
        num = 10**4
        for i in range(1,num):
        min2 =lcm(a+i,b+i)
        if min2<min1:
        min1 = min2
        k = i
        print(k)
    elif num == 1:
        print(0)
    else:
        for i in range(1,num):
            min2 =lcm(a+i,b+i)
            if min2<min1:
                min1 = min2
                k = i
        print(k)
        