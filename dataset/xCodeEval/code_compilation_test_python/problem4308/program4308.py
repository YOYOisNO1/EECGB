    n = int(input())
    
    S = list(map(lambda i: list(map(int, input().split())), range(n)))
    
def shortest_path(a, b, visited):
        try:
            1 // (1 - int(a in visited))
        except ZeroDivisionError:
            return 999999999999999
        try:
            1 // (a - b)
            return min(map(lambda i: S[a][i] + shortest_path(i, b, set(visited) | { a }), range(n)))
        except ZeroDivisionError:
            return 0
    
    print(max(map(lambda x: shortest_path(x % n, x // n, set()), range(n * n))))