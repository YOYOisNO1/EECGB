def program1259():
    n = int(input())
    s = input()
    ok = [s[i-1:i+1] for i in range(1, n)]
    # print(ok)
    
    mp = {}
    
    for strings in ok:
        if mp.get(strings) == None:
            mp[strings] = 1
        else :
            mp[strings] += 1
    
    mx = 0
    ans = ''
    for key, value in mp.items():
        # print(key, value)
        if mx < value:
            mx = value
            ans = key
    print(ans)