def program1573():
    c, d = list(map(int, input().split()))
    n, m = list(map(int, input().split()))
    f = n * m
    k = int(input())
    result = 0
    uch = k
    
    useosn = usedop = 0
    
    while uch < f:
        if c/n < d:
            result += c
            uch += n
        else:
            result += d
            uch += 1
    
    
    
    print(max(0, result))
    
    
    