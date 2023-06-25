def program208():
    s = list(input())
    r = 1
    ans = 0
    for i in range(len(s)):
        a = abs((ord(s[i])-96)-r)
        if a>14 : 
            ans += 26-a
            r = 26 - (ord(s[i])-96)
        else:
            ans += a
            r = ord(s[i])-96
        
    print(ans)