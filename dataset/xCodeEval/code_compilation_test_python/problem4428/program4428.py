def program4428():
    import sys
    from collections import deque
    
    n, x, y = map(int, input().split())
    ans = 0
    dq = deque()
    
    for i in range(1, n+1):
        ans += x
        while dq and dq[0][1] < i:
            dq.popleft()
        if dq:
            ans = min(ans, dq[0][0] - i*x)
    
        ycost = ans + y + x*(i*2)
        while dq and dq[-1][0] > ycost:
            dq.pop()
        dq.append((ycost, i*2))
    
    print(ans)