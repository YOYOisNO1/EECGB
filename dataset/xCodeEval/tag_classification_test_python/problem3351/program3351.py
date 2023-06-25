    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    
def solve(n, a, b, c):
        if n == 1 :
            return 0
        if a == min(a, b, c):
            return (n-1)*a
        if b == min(a, b, c):
            return (n-1)*b
        return min(a, b) + (n-2)*c
    print(solve(n,) a, b, c)