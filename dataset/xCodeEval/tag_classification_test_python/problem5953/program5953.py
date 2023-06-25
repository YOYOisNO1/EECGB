def gcd(a, b): 
        while b != 0: 
            a, b = b, a % b 
        return a
    
    
    n = int(input())
    crash = list(map(int, input().split()))
    s = set()
    
    t = 1
    for i in range(n):
        counter = 1
        j = crash[i] - 1
    
        while j != i and counter <= n:
            counter += 1
            j = crash[j] - 1
        if counter > n:
            t = -1
            break
        else:
            #print(counter)
            if counter % 2 == 0:
                counter //= 2
            t = (t * counter) // gcd(t, counter)
            
    print(t)