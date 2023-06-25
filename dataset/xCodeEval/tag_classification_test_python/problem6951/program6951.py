    import os,sys
    from random import randint, shuffle
    from io import BytesIO, IOBase
    
    from collections import defaultdict,deque,Counter
    from bisect import bisect_left,bisect_right
    from heapq import heappush,heappop
    from functools import lru_cache
    from itertools import accumulate, permutations
    import math
    
    # Fast IO Region
    BUFSIZE = 8192
    class FastIO(IOBase):
        newlines = 0
    def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
    def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
    def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()
    def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)
    class IOWrapper(IOBase):
    def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    
    
    # for _ in range(int(input())):
    #     n = int(input())
    #     a = list(map(int, input().split()))
    
    # for _ in range(int(input())):
    #     n = int(input())
    #     ans = n + n // 2 * 2 + n // 3 * 2
    #     print(ans)
    
    # for _ in range(int(input())):
    #     n, k, r, c = list(map(int, input().split()))
    #     ans = [['.'] * n for _ in range(n)]
    #     r -= 1
    #     c -= 1
    #     for i in range(n):
    #         for j in range(n):
    #             if (i + j) % k == (r + c) % k:
    #                 ans[i][j] = 'X'
    #     for i in range(n):
    #         print(''.join(ans[i]))
    
    # for _ in range(int(input())):
#     def solve():
    #         n = int(input())
    #         a = list(map(int, input().split()))
    #         b = list(map(int, input().split()))
    #         for i in range(n):
    #             if a[i] > b[i]:
    #                 print('NO')
    #                 return
    #             if b[i] > b[(i + 1) % n] + 1 and a[i] < b[i]:
    #                 print('NO')
    #                 return
    #         print('YES')
    #     solve()
    
    # mod = 10 ** 9 + 7
    # N = 501000
    # fac = [1] * N
    # for i in range(2, N):
    #     fac[i] = fac[i - 1] * i % mod
    # invfac = [1] * N
    # invfac[N - 1] = pow(fac[N - 1], mod - 2, mod)
    # for i in range(N - 1)[::-1]:
    #     invfac[i] = invfac[i + 1] * (i + 1) % mod
# def c(i, j):
    #     return fac[i] * invfac[j] * invfac[i - j] % mod
    # n, k = list(map(int, input().split()))
    # if k >= n:
    #     print(pow(2, n, mod))
    # else:
    #     ans = 0
    #     a = [0] * (k + 1)
    #     for i in range(k + 1):
    #         a[i] = c(n - 1, i)
    #     ans = sum(a) * 2 - a[-1]
    #     print(ans % mod)
    
    n = 30
    s = defaultdict(set)
    # s = set()
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if n - i - j > 0:
                ans += 1
                s[math.gcd(i, j)].add(n - i - j)
                # s.add((math.gcd(i, j), n - i - j))
    # print(s, ans)
    
    N = int(pow(10 ** 9, 0.5)) + 5
def get_prime_linear(n):
        global cnt
        for i in range(2, n + 1):
            if not st[i]:
                primes[cnt] = i
                cnt += 1
            for j in range(n):
                if primes[j] > n / i: break
                st[primes[j] * i] = True
                if i % primes[j] == 0: break 
    primes, cnt, st = [0] * (N + 5), 0, [False] * (N + 5)
    get_prime_linear(N)
    prime1e3 = primes[:cnt]
    @lru_cache(None)
def get_factor(n):
        res = []
        for i in prime1e3:
            if i * i > n:
                break
            while n % i == 0:
                n //= i
                res.append(i)
        if n > 1:
            res.append(n)
        return set(res)
    
    @lru_cache(None)
def calc(k):
        cnt = k - 1
        s = list(get_factor(k))
        n = len(s)
        for i in range(1 << n):
            p = 1
            cnt1 = 0
            for j in range(n):
                if i >> j & 1:
                    cnt1 += 1
                    p *= s[j]
            if p != 1 and p != k:
                if cnt1 % 2:
                    cnt -= k // p - 1
                else:
                    cnt += k // p - 1
        return cnt
    
    # for i in range(1, 100):
    #     cnt = 0
    #     for j in range(1, i):
    #         if math.gcd(j, i - j) == 1:
    #             cnt += 1
    #     print(i, calc(i), cnt)
    
def lcm(x, y):
        return x * y // math.gcd(x, y)
    n = int(input())
    ans = 0
    st = set()
    for g in range(1, n + 1):
        mx = n - 2 * g
        if mx > 0:
            for c in range(mx, -10, -g):
                if c <= 0: break
                k = (n - c) // g
                cnt = calc(k)
                ans += cnt * lcm(g, c)
    print(ans % (10 ** 9 + 7))
    
    
    
    
                