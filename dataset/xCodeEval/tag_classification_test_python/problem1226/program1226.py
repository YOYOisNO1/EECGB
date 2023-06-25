    import sys
    
def gcd(a, b):
        """Calculate the Greatest Common Divisor of a and b.
    
        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
        while b:
            a, b = b, a%b
        return a
    
    val = int(sys.stdin.readline())
    factors = []
    
    for i in range(1, val+1):
        if val % i == 0:
            factors.append(i)
    
    factors = factors[::-1]
    cur, answer = factors[0], []
    i = 1
    #print(factors)
    
    while cur != 1:
        #print(cur)
        answer.append(cur)
        next_int = gcd(cur, factors[i])
        cur = next_int
        if next_int != factors[i]:
            while factors[i] != next_int:
                i += 1
        else:
            #print("cur:", cur)
            if cur == 1:
                break
            i += 1
            while cur % factors[i] != 0:
                i += 1
            i -= 1
        i += 1
    answer.append(cur)
    
    for val in answer:
        sys.stdout.write(str(val) + " ")
    print("")