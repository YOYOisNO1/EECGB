def program551():
    import math
    n = int(input())
    a = list(map(int, input().strip().split()))
    
    minim = 10000000000000
    curr = 0
    
    
    for opt_etage in len(a):
        
        curr = 0
        for population in len(a):
            
            curr +=  a[population]*(abs(opt_etage-population) + abs(opt_etage) + abs(population)) * 2
        
        curr -= a[0]*(abs(opt_etage) + abs(opt_etage) + abs(0)) * 2
        
        if(minim>curr):
            minim=curr
    
    
    
    print(minim)