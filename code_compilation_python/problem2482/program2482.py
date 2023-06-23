def program2482():
    
     a,b=map(int,input().split())
    c=[0]*18
    for d in range(1,7):c[abs(a-d)-abs(b-d)]+=1
    print sum(c[-7:]),c[0],sum(c[1:7])