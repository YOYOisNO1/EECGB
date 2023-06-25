    n, b = map(int, input().strip().split(" "))
    primes = {}
    
    
def get(p):
        result = 0
        nx = n
        while nx:
            result += nx//p
            nx //= p
        return result
    
    
def divide():
        x = b
        i = 2
        while i*i <= x:
            while x % i == 0:
                if i not in primes:
                    primes[i] = 0
                primes[i] += 1
                x //= i
            i += 1
        if x > 1:
            if x not in primes:
                primes[x] = 1
            else:
                primes[x] += 1
    
    
def check(val):
        for k, v in primes.items():
            if get(k) < val*v:
                return False
        return True
    
    
    divide()
    # print(primes)
    left = 0
    right = 10**20
    result = 0
    while left+1 < right:
        mid = (left+right)//2
        if check(mid):
            result = max(result, mid)
            left = mid+1
        else:
            right = mid-1
    
    for i in range(left, right+1):
        if check(i):
            result = max(result, i)
    print(result)