    N = int(input())
    M = 10 ** 8 + 5
    pr = [True] * M
    pr[0], pr[1] = False, False
    for i in range(2, M):
        if pr[i]:
            for j in range(i * 2, M, i):
                pr[j] = False
    
    prime = list(filter(lambda x: pr[x], range(M)))
    
    
def calc(n, k):
        if n == 0:
            return k
        elif n % 2 == 0:
            return n // 2 + k
        else:
            for i in prime:
                if n % i == 0:
                    n -= i
                    return calc(n, k + 1)
    
    
    print(calc(N, 0))