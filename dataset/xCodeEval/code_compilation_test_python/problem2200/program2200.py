def program2200():
    n,p=map(int,input().split())
    
            
    if p>=n:
        print(-1)
    else:
        nn=n
        j=1
        while True:
            nn-=p
            if bin(nn).count("1")<=j and nn>=j:
                ans=j
                break
            j+=1
        
        print(j)
       # print(ans)
        