def program3822():
    s = input()
    
    y = x = 0
    
    used = [False for i in xrange(200)]
    
    for c in s:
        if c >= '0' and c <= '9':
            continue
        elif c == '?':
            x += 1
        elif not used[ord(c)]:
            y += 1
            used[ord(c)] = True
            
    if s[0] == '?':
        ans = 9
        x -= 1
        while x:
            ans *= 10
            x -= 1
        z = 10
        while y:
            ans *= z
            z -= 1
            y -= 1
        print(ans)
    elif s[0] >= '0' and s[0] <= '9':
        ans = 1
        while x:
            ans *= 10
            x -= 1
        z = 10
        while y:
            ans *= z
            z -= 1
            y -= 1
        print(ans)
    else:
        ans = 9
        y -= 1
        while x:
            ans *= 10
            x -= 1
        z = 9
        while y:
            ans *= z
            z -= 1
            y -= 1
        print(ans)
            