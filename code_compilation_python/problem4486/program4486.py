def program4486():
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
        while edges < m:
            tries += 1
            if (n>=1000) and (tries > 1):
                break
            edges = 0
            newgraf = set([])
            usedonce = set([])
            usedtwice = set([])
            listv = (range(1,n+1))
            listu = (range(1,n+1))
            random.shuffle(listv)
            random.shuffle(listu)
            
            for v in listv:
                if edges>=m:
                    break
                for u in listu:
    #                print "viewing:", u,v
                    if v==u:
    #                    print "the same"
    #                    print
                        continue
                    if u in usedtwice:
    #                    print "u used twice"
    #                    print
                        continue
                    if v in usedtwice:
    
    #                    print "v used twice"
    #                    print
                        break
        
                    if ((u,v) in graf) or ((v,u) in graf):
    #                    print "edge in old graf"
    #                    print
                        continue
                    if ((u,v) in newgraf) or ((v,u) in newgraf):
    #                    print "edge already added"
    #                    print
                        continue
        
                    newgraf.add((u,v))
                    edges += 1
    #                print "adding edge",u,v
    #                print "now edges:", edges
                    if edges >= m:
                        break
                    if u in usedonce:                
                        usedtwice.add(u)
                    else:
                        usedonce.add(u)
                    if v in usedonce:
                        usedtwice.add(v)
                        #continue
                    else:
                        usedonce.add(v)
    #                print "usedonce:", usedonce
    #                print "usedtwice:", usedtwice
    #                print
    #                print
        if (n>=1000) and (tries > 1):
            print -1
        else:
            for e in newgraf:
                print e[0], e[1]
                
    
    
        
    
    
    
    