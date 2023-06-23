def program142():
    a = 'abcdefghijklmnopqrstuvwxyz'
    
    s = input().lower()
    ans = 'YES'
    
    n = [a.index(s[0]) + 1, a.index(s[1]) + 1]
    
    for i in range(2, len(s)):
        if n[i - 2] + n[i - 1] - 1 > 26:
            if a.index(s[i]) + 1 == n[i - 2] + n[i - 1] - 27:
                n.append(a.index(s[i]) + 1)
            else:
                ans = 'NO'
                break
        else:
            if a.index(s[i]) + 1 == n[i - 2] + n[i - 1] - 1:
                n.append(a.index(s[i]) + 1)
            else:
                ans = 'NO'
                break
    print(ans)