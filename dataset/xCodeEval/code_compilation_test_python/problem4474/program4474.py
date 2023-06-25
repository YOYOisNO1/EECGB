    __author__ = 'Darren'
    
    
    # d(x) = (x-1) % 9 + 1
def solve():
        n = int(input())
    
        # count[i]: the number of x's in [1,n] such that d(x) = i
        count = [0] * 10
        for i in range((n-1) % 9 + 2):
            count[i] = (n + 8) // 9
        for i in range((n-1) % 9 + 2, 10):
            count[i] = n // 9
    
        result = 0
    
        # Count all triples (i, j, k) such that d(d(i)*d(j)) = d(k)
        for i in range(1, 10):
            for j in range(1, 10):
                result += count[i] * count[j] * count[(i*j-1) % 9 + 1]
    
        # For each i, there are n/i triples (i,j,k) such that i*j = k,
        # i.e., the correct cases
        for i in range(1, n+1):
            result -= n // i
    
        print(result)
    
    
    if __name__ == '__main__':
        solve()