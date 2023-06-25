def program4657():
    import sys
    
    stuff = [int(i) for i in input().split()]
    
    n = stuff[0]
    k = stuff[1]
    
    first = {}
    last = {}
    
    s = list(input())
    
    for i in xrange(n):
        if s[i] not in first:
            first[s[i]] = i + 1
        last[s[i]] = i + 1
    
    combined = []
    
    for i in first:
        combined.append((first[i], 1))
    
    for i in last:
        combined.append((last[i] + 1, -1))
    
    combined = sorted(combined)
    
    cur = 0
    cur_guards = 0
    
    while cur < len(combined):
        day = combined[cur][0]
        cur_guards += combined[cur][1]
        cur += 1
        if cur < len(combined) and combined[cur][0] == day:
            cur_guards += combined[cur][1]
            cur += 1
        if cur_guards > k:
            print("YES")
            sys.exit()
    
    print("NO")