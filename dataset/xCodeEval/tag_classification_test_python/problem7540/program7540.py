    n, m, k = map(int, input().split())
    
def can_move(m, k):
        if k == 1 and m > 1:
            return True
    
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0 and m / i >= k:
                return True
    
        return False
    
    
def answer(n, m, k):
        # if n is even, Marsel wins. he just symmetrically repeats moves of Timur
        if n % 2 == 0:
            return "Marsel"
    
        # now consider a case of odd n
        assert n % 2 == 1
    
        # if Timur cannot move - he is losing automatically
        if not can_move(m, k):
            return "Marsel"
    
        # if he can do a move, he always can split one log into few parts that this
        # parts cannot be splitted again
        return "Timur"
    
    
    print(answer(n, m, k))