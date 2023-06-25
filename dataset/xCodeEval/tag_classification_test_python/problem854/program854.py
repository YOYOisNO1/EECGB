    s = list(input().strip())
    r = list(input().strip())
    
def calc(str):
        if str == '+':
            return 1
        elif str == '-':
            return -1
        else:
            return 0
    
    res = 0
    for str in s:
        res += calc(str)
    
    cur = []
    for i in r:
        h = calc(i)
        curNow = []
    
        if len(cur):
            for c in cur:
                if h != 0:
                    curNow.append(c + h)
                else:
                    curNow.append(c + 1)
                    curNow.append(c - 1)
        else:
            if h != 0:
                curNow.append(h)
            else:
                curNow.append(-1)
                curNow.append(1)
    
        cur = curNow
    
    sum = len([x for x in cur if x == res])/len(cur)
    
    print("%1.10f" % (sum))
    
    
    