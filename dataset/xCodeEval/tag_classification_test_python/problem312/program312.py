def program312():
    n = int(input())
    #sum = n*(n+1)/2
    #for i in xrange(1, n+1, 2):
    #  sum -= 2*i
    
    print(n/2) if n % 2 == 0 else -(n+1)/2
    