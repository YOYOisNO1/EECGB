    
def dfs(n):
    
        bool[n] = True
        for i in hash[n]:
            if bool[i] == False:
                dfs(i)
    
    
    from collections import defaultdict
    
    hash = defaultdict(set)
    
    n,m = map(int,input().split())
    flag = 0
    for i in range(m):
        a,b = map(int,input().split())
        hash[a].add(b)
        hash[b].add(a)
    mini = 10**18
    for i in range(1,8):
        for j in range(1,8):
            if i!=j:
                mini = min(len(hash[i]&hash[j]),mini)
    
    print(m-mini)
    
    
    
    
    
    