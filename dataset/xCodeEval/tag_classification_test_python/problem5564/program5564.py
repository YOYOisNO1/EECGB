def solve():
        b = [n // m for _ in range(m)]
        x = n % m
        for i in range(x):
            b[i] += 1
        return ' '.join(map(str, b))
    
    
def main():
        global n, m
        n, m = map(int, input().split())
        print(solve())
    
    
    main()