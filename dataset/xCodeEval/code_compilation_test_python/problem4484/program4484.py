def program4484():
    import random
    s = input().split()
    
    n = int(s[0])
    m = int(s[1])
    
    graf = set([])
    
    for i in xrange(m):
        s = input().split()
        u = int(s[0])
        v = int(s[1])
        graf.add((u,v))
        
        #print graf
    if m*4>n*(n-1):
        print -1
    else:
        edges = 0
        tries = 0
        listv = range(1,n+1)
        while edges < m:
            tries += 1
            if (tries > 10000):
                break
            edges = 0
    
            random.shuffle(listv)
            for i in xrange(m):
                u = listv[i-1]
                v = listv[i]
                edges = i+1
                if ((u,v) in graf) or ((v,u) in graf):
                    edges = 0
                    break
    
        if (tries > 10000):
            print -1
        else:
            for i in xrange(m):
                print listv[i-1], listv[i]
                
    
    
        
    
    
    
    