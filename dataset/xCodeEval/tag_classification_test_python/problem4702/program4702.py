def program4702():
    
    n, k = input().split()
    n = int(n)
    k = int(k)
    
    inp = input()
    '''
    
    n = 9
    k = 2
    inp = 'AHHBAAAAH'
    '''
    s = []
    e = []
    seen = set()
    
    for c in inp:
        if c not in seen:
            s.append('s')
            seen.add(c)
        else:
            s.append('.')
    
    seen = set()
    
    for i in range (len(inp)-1, -1, -1):
        if inp[i] not in seen:
            e.append('e')
            seen.add(inp[i])
        else:
            e.append('.')
    
    e = e[::-1]
    
    cnt = 0
    maxcnt = 0
    
    for i in range (len(inp)):
        if s[i] == 's':
            cnt += 1
    
        maxcnt = max(cnt, maxcnt)
    
            
        if e[i] == 'e':
            cnt -= 1
    #print((maxcnt))
    
    if maxcnt > k:
        print(("YES"))
    else:
        print(("NO"))
    
    
    '''
    print((s))
    print((e))
    '''
    
    '''
    open_doors = 0
    current = []
    opened = False
    
    for i in range (len(s)):
        if opened == False:
            current.append(s[i])
            opened = True
    
        else:
            if s[i] not in current:
                open_doors += 1
            else:
                current.remove(s[i])
                opened = False
    
    #print((open_doors))
    
    if open_doors >= k:
        print(("YES"))
    
    else:
        print(("NO"))
    '''            