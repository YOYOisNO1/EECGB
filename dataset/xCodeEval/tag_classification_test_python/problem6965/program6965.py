def program6965():
    lijst = input().split()
    n = int (lijst[0])
    d = float (lijst[1])
    
    kans = 0
    k = 0
    while (kans < d):
        k+=1 
        kans = 1-((n-k)*(n-k-1)*(n-k-2)/6 + 0.5 *k*(n-k)*(n-k-1)/2)/(n*(n-1)*(n-2)/6)
    
    print(k)