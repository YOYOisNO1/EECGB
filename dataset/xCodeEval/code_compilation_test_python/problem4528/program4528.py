def BinPow(a,n):
        if n = 1:
            return a
        elif n % 2 == 0:
            return BinPow(a * a, n // 2)
        else:
            return a * BinPow(a * a, n // 2)
    
    print(BinPow(2,int(input()))+1)