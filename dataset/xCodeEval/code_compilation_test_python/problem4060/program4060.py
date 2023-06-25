    n, q = map(int, input().split())
    
    fr = dict()
    past = dict()
    for i in range(q):
        a, b = input().split()
        if b in fr:
            fr[b].append(a)
        else:
            fr[b] = [a]
    
    
def dfs(c, cnt):
        global n
        if cnt == n:
            return 1
        if cnt > n:
            return 0
        global past
        p = ord(c) + cnt*1000
        if p in past:
            return past[cnt]
        
        global fr
        if c not in fr:
            return 0
        
        ans = 0
        for i in fr[c]:
            ans += dfs(i[0], cnt+1)
        past[p] = ans
        return ans
    
    
    print(dfs('a', 1))