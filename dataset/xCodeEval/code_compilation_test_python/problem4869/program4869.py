def program4869():
    n, m, l = map(int, input().split())
    
    planet = []
    
    for i in xrange(n):
        nome = input()
        op = []
        for j in xrange(m):
            
            a, b, c = map(int, input().split())
    
            op.append([a, b, c])
    
        planet.append(op)
    
    
    maximo = 0
    
    for i in xrange(n):
        for j in xrange(n):
            if i != j:
                pft = []
                for k in xrange(m):
                    luc = (planet[j][k][1] - planet[i][k][0])*planet[i][k][2]
                    pft.append([luc, planet[i][k][2]])
                               
                pft.sort(reverse=True, key=lambda tup:tup[0])
    
                qtd = 0
                ganho = 0
                for r in xrange(len(pft)):
                    if qtd + pft[r][1] < l and pft[r][0] > 0:
                        ganho += pft[r][0]
                        qtd += pft[r][1]
                    elif pft[r][0] > 0:
                        ganho += (pft[r][0]/pft[r][1])*(l-qtd)
                        break
                    else:
                        break
                              
    
                if ganho > maximo:
                    maximo = ganho
    
    print maximo