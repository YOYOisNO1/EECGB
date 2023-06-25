def program748():
    #code
    
    R = lambda:map(int,input().split())
    
    c, v, u, a, l = R()
    
    ans=1
    c-=v
    while c>0:
        ans+=1
        v=min(u,v+a)
        c-=v-l
    print(ans)