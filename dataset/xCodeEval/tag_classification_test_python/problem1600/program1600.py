    #map(int,input().split())
    #for gg in xrange():
def factors(n):    
        return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
    n,x=map(int,input().split())
    count=0
    for gg in factors(x):
        if (max(gg,(x/gg))<=n):
            count=count+1
    print(count)