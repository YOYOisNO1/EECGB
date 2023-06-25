def program4521():
    n = int(input())
    
    l = list(range(2,1000001))
    i = 0
    while i <= len(l)-1:
        div = l[i]
        if n%(div**2) == 0:
            n = n//div
        else:
            i+=1
            
    print(n)