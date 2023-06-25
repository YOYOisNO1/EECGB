def program5955():
    import math
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))!=len(a): print(-1)
    else:
        ans,cycle=None,None
        visited=[False]*(n+1)
        for i in range(n):
            if visited[i+1]: continue
            count,v=0,[]
            index,value=i+1,-1
            while value!=i+1:
                visited[index]=True
                v.append(index)
                value=a[index-1]
                index=value
            cycle=[len(v)//2,len(v)][len(v)%2]
            if i==0: ans=cycle
            else: ans=(ans*cycle)//math.gcd(ans,cycle)
        print(ans)