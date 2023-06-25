def program4717():
    t=input()
    
    m1,n1 = map(int, input().split())
    m2,n2 = map(int, input().split())
    m3,n3 = map(int, input().split())
    a=m1
    b=m2
    c=m3
    if a+b+c==t:
        print(a,b,c)
    else:
        a=min(n1,t-b-c)
        b=min(n2,t-a-c)
        c=min(n3, t-a-b)
        print(a,b,c)