def program1504():
    l1,r1,l2,r2,k = map(int,input().split())
    
    if r1<l2 or r2<l1:
        print(0)
    else:
        st,end = (max(l1,l2),min(r1,r2))
        if st<=k<=end:
            print(end-st)
        else:
            print(end-st+1)
    
    
    
    