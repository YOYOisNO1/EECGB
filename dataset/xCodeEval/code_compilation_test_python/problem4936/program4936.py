def program4936():
    import math
    n_and_c=input().split(' ')
    n=int(n_and_c[0])
    c=int(n_and_c[1])
    count=0
    i=1
    while i<=n:
        count+=math.factorial(c+i-1)/(math.factorial(c-1)*math.factorial(i))
        i+=1
    print count
    print count % (10**6+3)