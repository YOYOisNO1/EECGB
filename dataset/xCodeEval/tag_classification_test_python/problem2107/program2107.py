    #!/usr/bin/pypy3
    
    from sys import stdin,stderr
    
def readInts(): return map(int,stdin.readline().strip().split())
def print_err(*args,**kwargs): print(*args,file=stderr,**kwargs)
    
def naive_kt(k,d,n):
        if n<0: return 0
        if n<d: return 0
        if n==0: return 1
        s = 0
        for i in range(1,k+1):
            d2 = 0
            if i>=d: d2 = 0
            else: d2 = d
            s += naive_kt(k,d2,n-i)
        return s
    
def dp_kt(k,d,n):
        a_d_used = [1]
        a_d_unused = [0]
        for ni in range(1,n+1):
            s = 0
            for si in range(max(0,ni-k),ni):
                s += a_d_used[si]
            a_d_used.append(s)
        for ni in range(1,n+1):
            s = 0
            for si in range(1,k+1):            
                if ni-si<0: continue
                v = a_d_unused[ni-si]
                if si>=d: v = a_d_used[ni-si]
                s += v
            a_d_unused.append(s)
        return a_d_used,a_d_unused
    
def solve(vs):
        return None
    
def run():
        modval = 10**9+7
        n,k,d = readInts()
        _, dp = dp_kt(k,d,n)
        print(dp[-1] % modval)
            
    run()