    p = 998244353
    
    triangle = [[1], [1, 1]]
    for i in range(2, 501):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append((triangle[-1][j-1]+triangle[-1][j]) % p)
        row.append(1)
        triangle.append(row)
        
    
    
def process(n, k):
        d = [[0 for i in range(k+1)] for j in range(n)]
        """
        d[n1][k1] = # of sequences of length n
        where the ai are at most k
        
        """
        for i in range(k+1):
            d[0][i] = 1
        for n1 in range(1, n):
            """
            if the ai are all 1
            then there are n1*(n1-1)//2 edges
            """
            d[n1][0] = 1
            exp = n1*(n1-1)//2
            d[n1][1] = pow(k, exp, p)
        for k1 in range(2, k+1):
            for n1 in range(1, n):
                for l in range(n1+1):
                    entry1 = triangle[n1][l]
                    exp = (l*(l-1)//2+(n1-l)*l) % (p-1)
                    entry2 = pow(k-k1+1, exp, p)
                    entry3 = d[n1-l][k1-1]
                    d[n1][k1]+=(entry1*entry2*entry3) % p
                d[n1][k1] = d[n1][k1] % p
        return d[n-1][k]
    
    n, k = [int(x) for x in input().split()]
    print(process(n, k))