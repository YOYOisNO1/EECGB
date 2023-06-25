def program3092():
    n,v=map(int,input().split())
    ans=0
    curr=0
    i=1
    n-=1
    while n:
        if curr<n:
            
            cst=min(v-curr,n-curr)
            #print(cst,i)
            ans+=(cst*i)
            curr+=cst
        
        n-=1
        curr-=1
        i+=1
    print(ans)