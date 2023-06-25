    import sys
    
def read_ints():
        return [int(i) for i in sys.stdin.readline().strip().split()]
    
def read_int():
        return int(sys.stdin.readline().strip())
    
    CACHE = {}
    
def n_ones(n):
        if n < 5:
            return n
        if n in CACHE:
            return CACHE[n]
    
        n = abs(n)
        s = str(n)
        ones = int("1" * len(s))
        dig = int(s[0])
        guess = ones * dig
        if n == ones:
            return len(s)
        elif guess <= n:
            below = guess
            if dig == 9:
                above = int("1" * (len(s) + 1))
            else:
                above = guess + ones
        else:
            above = guess
            if dig == 1:
                below = int("9" * (len(s) - 1))
            else:
                below = guess - ones
    
        above_digit = int(str(above)[0])
        below_digit = int(str(below)[0])
    
        #print("n: %d above2: %d" % (n, above2))
    
    
        below_ones = below_digit * len(str(below)) + n_ones(n - below)
        above_ones = above_digit * len(str(above)) + n_ones(above - n)
    
        #print("n %d above %d below %d above_ones %d below_ones %d" % (n, above, below, above_ones, below_ones))
        result = min(below_ones, above_ones)
    
        if dig > 5:
            above2 = int("1" * (len(s) + 1))
            above2_digit = int(str(above2)[0])
            above2_ones = above2_digit * len(str(above2)) + n_ones(above2 - n)
            result = min(result, above2_ones)
    
        CACHE[n] = result
        return result
    
    
    """
    assert n_ones(1) == 1
    assert n_ones(2) == 2
    assert n_ones(5) == 5
    assert n_ones(9) == 4 # 11 - 1 - 1
    assert n_ones(24) == 6 # 11 + 11 + 1 + 1
    assert n_ones(97) == 8 # 111 - 11 - 1 - 1 - 1
    assert n_ones(98) == 7 # 111 - 11 - 1 - 1
    assert n_ones(99) == 6 # 111 - 11 - 1
    assert n_ones(111) == 3 # 111
    assert n_ones(102) == 7 # 111 - 11 + 1 + 1
    assert n_ones(529) == 23
    """
    
    n = read_int()
    print(n_ones(n))
    