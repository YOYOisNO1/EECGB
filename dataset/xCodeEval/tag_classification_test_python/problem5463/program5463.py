def solve(n, m, k, x, y):
        if n <= 2:
            cycle = n*m
            q1, q2, q3, k = k//cycle, k//cycle, k//cycle, k%cycle
            q1 += k>0
            q3 += k >= m*(x-1) + y
            return q1, q2, q3
        else:
            cycle = (2*n-2)*m
            if k < cycle:
                q1 = int(k > 0) + int(k > n*m)
                q2 = int(k >= n*m)
                q3 = int(k >= m*(x-1) + y) + int(x < n and k >= m*(2*n-x-1) + y)
                return q1, q2, q3
            q1, q2, k = 2*(k//cycle), k//cycle, k%cycle
            q3 = q1 if 1 < x < n else q2
            q1 += (k > m) + (k > n*m)
            q2 += k>= n*m
            q3 += (k >= m*(x-1) + y) + ((x < n) and (k >= m*(2*n-x-1) + y))
            return q1, q2, q3
    
    
    n, m, k, x, y = map(int, input().split())
    q1, q2, q3 = solve(n, m, k, x, y)
    print(q1, q2, q3)