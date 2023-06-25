    # from math import sqrt
# def prime_generator(n):
    #     primes = [2]
    #     for itter in range(2, n):
    #         prime = True
    #         for j in primes:
    #             if itter%j == 0:
    #                 prime = False
    #                 break
    #         if prime:
    #             primes.append(itter)
    #     return primes
def prime_generator(n):
        # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
        """ Input n>=6, Returns a list of primes, 2 <= p < n """
        correction = (n%6>1)
        n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
        sieve = [True] * (n//3)
        sieve[0] = False
        for i in range(int(n**0.5)//3+1):
            if sieve[i]:
                k=3*i+1|1
                sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
                sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
        return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
    
    string = input().split()
    n = int(string[0])
    k = int(string[1])
    
    primes = prime_generator(n)
    length = 2
    nums = []
    i = 2
    while length != k+1:
        check = False
        check2 = False
        if length == k:
            # print("here")
            for i in range(2, 20):
                if n%i == 0 and n/i != 1:
                    n /= i
                    nums.append(i)
                    length += 1
                    check2 = True
                    break
        if check2:
            break
        for i in primes:
            if n%i == 0 and n/i != 1:
                n /= i
                nums.append(i)
                length += 1
                check = True
                break
        if not check:
            break
        # length += 1
    # print("length =", length)
    # print("num =", nums)
    if len(nums) != k-1:
        print(-1)
    else:
        for i in range(k-1):
            print(nums[i], end = " ")
        print(int(n))