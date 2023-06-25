    t=input()
    a=map(int,input().split())
    b=a[::2]
    c=a[1::2]
    print b,c
def cmp1(x):
        for i in range(1,len(x)):
            if (x[i]>x[i-1])==0:
                return False
def cmp2(x):
        for i in range(1,len(x)):
            if (x[i]<x[i-1])==0:
                return False
    if cmp1(b)==False or cmp2(c)==False or b[-1]>c[-1]:
        return 'no'
    else:
        return 'yes'