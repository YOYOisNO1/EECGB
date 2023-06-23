'''def f(n):
        n = [i-1 for i in n]
        a = []
        while max(n) >= 0:
            for i in range(len(n)-1,-1,-1):
                if n[i] != -1:
                    break
            k = [i]
            while n[k[-1]] != -1:
                k.append(n[k[-1]])
                n[k[-2]] = -1
            a.append(k[:-1])
        a.reverse()
        b = []
        for i in a: b += i
        return [i+1 for i in b]
    
    from recursive import permute
    
def g(n):
        k = permute([i+1 for i in range(n)])
        for i in k:
            if f(i) == i:
                print(i)
    '''
    
def F(n):
        a,b = 1,0
        for i in range(n):
            a,b = b,a+b
        return b
    
def ans(n,k):
        if n == 1: return [1]
        elif k > F(n):
            return [2,1] + [i+2 for i in ans(n-2,k-F(n))]
        else:
            return [1] + [i+1 for i in ans(n-1,k)]
    
    n,k = map(int,input().split())
    print(' '.join([str(i) for i in ans(n,k)]))