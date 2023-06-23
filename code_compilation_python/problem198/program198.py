    from sys import stdin
    from itertools import combinations
    
def func(arr):
        count=0
        for ele in arr:
            count+=(ord(ele)-96)
        return count    
    n,k=map(int,stdin.readline().split())
    s=stdin.readline().strip()
    s=sorted(s)
    ans=[]
    for c in combinations(s,k):
        cond=True
        for i in range(k-1):
            if ord(c[i+1])-ord(c[i])>=2:
                pass
            else:
                cond=False
                break
        if cond==True:
            ans.append(func(c))
        else:
            pass
    if len(ans)==0:
        print(-1)
    else:
        print(min(ans))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    