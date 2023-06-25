def program4601():
    from sys import exit
    
    n, k = map(int, input().split(' '))
    
    ns = input()
    
    bs = []
    
    for i in xrange(ord('A'), ord('Z') + 1):
        c = chr(i)
    
        start = ns.find(c)
        end = ns.rfind(c)
    
        if start != -1:
            bs.append((start, -1))
            bs.append((end, 1))
    
    bs.sort()
    
    pidr = 0
    
    for b in bs:
        pidr -= b[1]
    
        if pidr > k:
            print("YES")
            exit(0)
    
    print("NO")