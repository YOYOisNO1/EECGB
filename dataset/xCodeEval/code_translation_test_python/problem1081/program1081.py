def program1081():
    import math
    n=int(input())
    a=[int(i) for i in input().split()]
    l=[]
    for i in range(1,len(a)):
        l.append(abs(a[i-1]-a[i]))
    if(len(set(l))==1):
        if(a[1]>=a[0]):
            print(a[len(a)-1]+(l[0]))
        else:
            print(a[len(a)-1]-l[0])
    else:
        print(a[len(a)-1])