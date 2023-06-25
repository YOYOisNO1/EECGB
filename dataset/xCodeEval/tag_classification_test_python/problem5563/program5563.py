def solve():
        b = [str(n // m + (1 if i < n % m else 0)) for i in range(m)]
        return ' '.join(b)
    
    
def main():
        global n, m
        n, m = map(int, input().split())
        print(solve())
    
    
    main()