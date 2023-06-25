def program4624():
    n,k = map(int,input().split())
    ll = input()
    d = {}
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        d[i] = 0
    
    for i in ll:
        d[i] += 1
    
    lll = {}
    t = True
    for i in ll:
        lll[i] = 1
        d[i] -= 1
        if len(lll) > k:
            print('YES')
            t = False
            break
        if d[i] == 0:
            del lll[i]
    
    if t:
        print('NO')