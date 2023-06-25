def program6184():
    r1,c1,r2,c2=map(int,input().split())
    a1=abs(r1-r2)
    a2= abs(c2-c1)
    print((r1!=r2) and c1 !=c2)+1,(a1!=a2)+1 if a1%2 == a2%2 else 0,max(a1,a2)