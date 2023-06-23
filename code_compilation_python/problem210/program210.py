def program210():
    n = int(input())
    m = n
    a = [False,False]+[True]*(m-1)
    primes = []
    for i in range(2,m+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i,m+1,i):
                a[j] = False
    
    c = 0
    while(n != 0):
        p = n
        for i in primes:
            if n%i == 0:
                p = i
                break
        n -= p
        c += 1
        if n%2 == 0 :
            c += n//2
            break
    print(c)