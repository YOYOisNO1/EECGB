def program163():
    t = int(input())
    for _ in range(t):
        n,k,d = map(int,input().split())
        l1 = list(map(int,input().split()))
        ans=n
        thing = l1[:d]
        for j in range(n-d+1):  
            ans = min(ans,len(set(thing)))
            thing.pop(l1[j])
            thing+=l1[j+d]
            
        print(ans)