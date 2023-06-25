    import math
    
    
def check(i, j, k):
        a = []
        b = []
        for ii in range(len(i)):
            a.append(j[ii] - i[ii])
            b.append(k[ii] - i[ii])
        la = 0
        lb = 0
        scal = 0
        for ii in range(len(i)):
            la += a[ii] * a[ii]
            lb += b[ii] * b[ii]
            scal += a[ii] * b[ii]
        return (scal / (la * lb)) <= 0
    
    
def count(w):
        ans = []
        for i in range(len(w)):
            f = 1
            for j in w:
                if (w[i] == j):
                    continue
                for k in w:
                    if (w[i] == k or j == k):
                        continue
                    f &= check(w[i], j, k)
            ans += [i + 1] if f else []
        return [len(ans)] + ans
    
    
    
    n = int(input())
    w = []
    for i in range(n):
        w.append(list(map(int, input().split())))
    if (n < 20):
        print(*count(w), end='\n')
    else:
        print(0)