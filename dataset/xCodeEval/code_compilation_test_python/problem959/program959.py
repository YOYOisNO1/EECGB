def program959():
    t,s,q = input().split()
    t=int(t)
    s=int(s)
    q=int(q)
    
    if(s<t/q):
        print(2)
    else:
        print(1)