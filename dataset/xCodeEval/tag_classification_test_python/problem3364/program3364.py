def divisors(n):
        count = 0
        for i in xrange(1, int(n**0.5) + 1):
            if(n % i == 0):
                count += 2
        if(int(n**0.5) * int(n**0.5) == n):
            count -= 1
        return count
    print(divisors(int(input())))