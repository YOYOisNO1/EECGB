def program1970():
    n, pos, l, r = map(int, input().split())
    
    left = False
    right = False
    
    if l != 1:
        left = True
    if r != n:
        right = True
    
    ans = 0
    if left:
     if pos != l:
            pos = max(pos - 1, l)
            ans += 1
        while pos - 1 >= l:
            pos = max(pos - 1, l)
            ans += 1
        ans += 1
    if right:
        if pos != r:
            pos = min(pos + 1, r)
            ans += 1
        while pos + 1 <= r:
            pos = min(pos + 1, r)
            ans += 1
        ans += 1
    
    print(ans )