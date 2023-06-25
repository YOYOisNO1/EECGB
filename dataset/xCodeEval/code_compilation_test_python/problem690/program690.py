    n = int(input())
    N = int(n**0.5)
def eraSieve(N):
        poss = []
        isPrime = [1 for i in range(N+1)]
        for i in range(2,N+1):
            if isPrime[i]:
                if not n%i:
                    poss.append(i)
                    if len(poss) >= 3:
                        break
                for j in range(i, N+1, i):  # 从 i 开始不要紧，因为已经取走了，可以少一个乘法
                    isPrime[j] = 0
        return poss
    poss = eraSieve(N)
    if not poss:
        print(n)
    elif len(poss)>=2:
        print(1)
    else:
        p = poss[0]
        fail = 0
        while n > 1:
            if n % p:
                fail = 1
                break
            n //= p
        if fail:
            print(1)
        else:
            print(p)