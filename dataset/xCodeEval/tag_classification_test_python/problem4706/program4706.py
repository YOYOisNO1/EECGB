def program4706():
    l = input().split()
    
    n = int(l[0])
    k = int(l[1])
    
    s = input()
    
    lens = len(s)
    
    first = []
    fn = []
    last = []
    ln = []
    
    for i in range(lens):
        if s[i] not in first:
            first.append(s[i])
            fn.append(i)
        if s[lens - i - 1] not in last:
            last.append(s[lens - i - 1])
            ln.append(lens - i - 1)
    ln.sort()
    more = False
    d = 0
    ad = None
    rm = None
    while not more:
        if ad == None: 
            if len(fn)==0: break
            ad = fn.pop(0)
        if rm == None: rm = ln.pop(0)
        if ad < rm:
            d+=1
            ad = None
        elif ad > rm:
            d-=1
            rm = None
        else:
            ad=None
            rm=None
            if d+1 > k:
                more = True
    
        if d > k:
            more = True
    
    if more:
        print("YES")
    else:
        print("NO")