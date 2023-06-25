def findSame(a):
        notFound = True
        res = -1
        for i in range(1, len(a)):
            curA = a[0:i]
            if notFound:
                if a[i] in curA and a[i] != 0:
                    notFound = False;
                    res = i
        return res
    
    n = input()
    ai = list(map(int, input().split()))
    
    modif = ai
    inx = findSame(modif)
    while inx > 0:
        modif[inx] -= 1
        inx = findSame(modif)
        
    
    print(sum(modif))