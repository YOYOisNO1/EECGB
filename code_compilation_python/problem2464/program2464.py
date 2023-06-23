    #!/usr/bin/env python3.9
    
    "###t = int(input()) #on recupere un entier"
    "###a = [* map(int, input().split())] on récupere plusieurs entier sur une ligne"""
    primes = []
    
def isPrime(k):
        for premier in primes:
            if not(k%premier):
                return False
        primes.append(k)
        return True
    
def nb(i, m):
        if i*i > m:
            return 1
        else:
           return ( m- i*i)/i
    
    
    [n, m] = [* map(int, input().split())]
    
    res = 0 
    
    nbNonDiv = [m]
    
    candidats = [i for i in range(1,m+1)]
    
    
def majCandidats(i):
        global candidats
        toKeep = []
        for k in range(len(candidats)):
            if not(candidats[k]%i):
                toKeep.append(candidats[k])
        candidats = toKeep
    
    for i in range(2, n+1):
        if isPrime(i):
            majCandidats(i)
            nbNonDiv.append(len(candidats))
        else : 
            nbNonDiv.append(nbNonDiv[-1])
        
    res = m
    produit = m
    
    for i in range(1, n):
        produit = (produit *(nbNonDiv[i])) % 998244353
        res += produit
    
    tot = 0
    for i in range(1, n+1):
        tot += pow(m, i, 998244353)
    
    print(tot - res)
    
    
        
        
    
                    
                