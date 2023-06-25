def solve(n):
    
        row = [1] * n #nice way to create a list repeated with the same value for the given times
    
        for i in xrange(1, n):
    
            prevCol = 1
    
            for j in xrange(1, n):
    
                row[j] = row[j] + prevCol
                prevCol = row[j]
    
        print(row[n-1])
    
    
    if __name__ == "__main__":
    
        n = int(input())
        solve(n)