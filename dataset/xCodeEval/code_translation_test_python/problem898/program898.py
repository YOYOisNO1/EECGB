def program898():
    n, m = map(int, input().split())
    
    s = ''
    sm = 0
    for _ in range(n):
        temp = input().strip()
        if 'S' in temp:
            s += temp
        else:
            sm += len(temp)
            n -= 1
    
    for i in range(m):
        sm += ('S' not in s[i::m]) * n
    
    print(sm)