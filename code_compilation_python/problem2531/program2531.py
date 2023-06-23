    import math
    #525 63
    #20190929 1605
    #947 987654321987654321
def prime_factorization(n):
        sqrt_n = int(math.sqrt(n))
        bs = [False, False] + [True] * (sqrt_n-1)
        ps = []
        for i in range(2, sqrt_n+1):
            if bs[i]:
                if n % i == 0:
                    ps.append(i)
                for j in range(2*i, sqrt_n+1, i):
                    bs[j] = False
        ck = True
        # 자기자신이 소수일 경우
        for i in range(2, n):
            if n % i == 0:
                ck = False
        if ck:
            ps.append(n)
        return ps
    x, n = map(int, input().split())
    ps = prime_factorization(x) # 이 부분에서 시간이 많이 걸림, 수정필요
    # 에라토스테네스의 체를 응용함
    z = 1
    modulo = (10**9+7)
    for i in ps:
        c = 0
        for j in range(int(math.log(n, i)), 0, -1):
            f = i ** j
            nf = n//f
            z *= pow(f, (nf - c), modulo)
            # pow(x, y, z) == pow(x, y) % z (but more faster!!)
            # prevent overflow
            # a*b%c == ((a%c) * (b%c)) % c
            c = nf
    print(z % modulo)