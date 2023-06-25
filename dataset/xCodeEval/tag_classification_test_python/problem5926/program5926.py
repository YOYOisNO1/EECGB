def program5926():
    n = int(input())
    adj = [int(x) - 1 for x in input().split()]
    
    ans = 1
    
    from fractions import gcd
    lcm = lambda x, y : (x * y) // gcd(x, y)
    
    for i in range(n):
        visited = [0] * n
        visited[i] = 1
        j = adj[i]
        while visited[j] == 0:
            visited[j] = 1
            j = adj[j]
    
        if i != j:
            print(-1)
            exit()
        else:
            sm = sum(visited)
            if sm & 1:
                ans = lcm(ans, sum(visited))
            else:
                ans = lcm(ans, sm // 2)
    
    print(ans)
        