    """
    NTC here
    """
    import sys
    inp = sys.stdin.readline
def input(): return inp().strip()
    # flush= sys.stdout.flush
    # import threading
    # sys.setrecursionlimit(10**6)
    # threading.stack_size(2**26)
     
def iin(): return int(input())
     
     
def lin(): return list(map(int, input().split()))
     
     
    # range = xrange
    # input = input
     
def primetilln(n):
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
     
            if (prime[p] == True):
                for i in range(p * 2, n+1, p):
                    prime[i] = False
            p += 1
        primes = set()
        for i in range(2, n):
            if prime[i]:
                primes.add(i)
        return primes
     
def main():
    def check_palindrom(x):
            s = list(str(x))
            return s==s[::-1]
            
        T = 1
        while T:
            T-=1
            p, q = lin()
            mx = 10**7+10
            a = primetilln(mx-1)
            a1 = [0]*mx
            a2 = [0]*mx
            for i in a:a1[i]+=1
            for i in range(1, mx):
                if check_palindrom(i):
                    a2[i]+=1
            for i in range(1, mx):
                a1[i]+=a1[i-1]
                a2[i]+=a2[i-1]
            # print(a2[:20])
            ans = 0
            for i in range(1, mx):
                if a1[i]*q<=p*a2[i]:
                    ans=max(ans, i)
            print(ans if ans else "Palindromic tree is better than splay tree")
     
     
     
     
     
     
     
    main()
     
    # threading.Thread(target=main).start()