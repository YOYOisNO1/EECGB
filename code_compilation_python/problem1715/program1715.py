def program1715():
    
    n=int(input())
    a=int(input())
    b=int(input())
    c=int(input())
    x=n/a
    if ((n%a)-c)>0:
        x+=((n%a)-c)/(b-c))
    y=(n-c)/(b-c)+(((n-c)%(b-c))/a)
    print max(x,y)