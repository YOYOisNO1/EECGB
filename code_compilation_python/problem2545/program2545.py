def program2545():
    a1,b1,a2,b2,l,r=map(int,input().split())
    ks1=(l-b1)/a1
    ke1=(r-b1)/a1
    ks2=(l-b2)/a2
    ke2=(r-b2)/a2
    
    lst1=[]
    lst2=[]
    ks1=max(0,ks1)
    ke1=max(0,ke1)
    ks2=max(0,ks2)
    ke2=max(0,ke2)
    for i in range(ks1,ke1+2):
        if(a1*i+b1>=l and a1*i+b1<=r):
            lst1.append(a1*i+b1)
    for i in range(ks2,ke2+2):
        if(a2*i+b2>=l and a2*i+b2<=r):
            lst2.append(a2*i+b2)
    
    set1=set(lst1)
    set2=set(lst2)
    
    l=len(set1.intersection(set2))
    print l
        