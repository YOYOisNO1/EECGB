def program91():
    s = map(int, input().split())
    c = input()
    mp = {}
    
    
    for i in c:
        try:
            mp[i] += 1
        except:
            mp[i] = 1
    
    maxx = 0
    for key, value in mp.iteritems():
        if value > maxx:
            maxx = value
    
    if maxx > s[1]:
        print("NO")
    else:
        print("YES")