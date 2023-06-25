def program877():
    a,b,c=map(int,input().split())
    l=c*2
    x=min(a,b)
    l+=x*2
    if(b>a):
        b=b-a
        a=a-x
    else:
        a=a-b
        b=b-x
    if(a!=0 or b!=0):
        l+=1
    print(l)