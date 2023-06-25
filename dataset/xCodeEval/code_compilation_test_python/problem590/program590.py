def program590():
    G = list(input())
    
    while '4' in G:
    
        G[G.index('4')] = '1'
    
    while '7' in G:
    
        G[G.index('7')] = '2'
    
    k = ''.join(G)
    
    p = (k[0])*(2**(len(k)-1))
    print int(k,3) - p