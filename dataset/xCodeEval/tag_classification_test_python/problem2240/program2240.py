def program2240():
    n,k = map(int,input().split())
    primes = [True]*1001
    primes[0] = primes[1] = False
    
    primesList = list()
    
    i = 2
    while i*i<=n:
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j] = False
        i+=1
        
        
    for i in range(2,n+1):
        if primes[i]:
            primesList.append(i)
    
    cnt = 0
    
    for i in range(len(primesList)-1):
        if primesList[i]+primesList[i+1]+1 in primesList:
            #print(primesList[i]+primesList[i+1]+1)
            cnt+=1
    
    if cnt>=k:
        print("Yes")
    else:
        print("No")
            
                