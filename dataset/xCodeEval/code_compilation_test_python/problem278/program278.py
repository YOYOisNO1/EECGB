def program278():
    from itertools import permutations
    n = int(input())
    s = list(map(int,input()))
    A = s[:n]
    B = s[n:]
    C = list(permutations(B))
    m = 0
    l = 0
    p = 0
    for j in C:
        for i in range(n):
            if( A[i] < j[i]):
                if(l > 0):
                    break
                m += 1
            elif(A[i] > j[i]):
                if(m > 0):
                    break
                l += 1
        if(m == n or l == n):
            print("YES")
            p += 1
            break
        m = 0
        l = 0
    if(p == 0):
        print("NO")