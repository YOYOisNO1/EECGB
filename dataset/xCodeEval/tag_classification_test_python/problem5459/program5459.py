def program5459():
    I = lambda: int(input())
    IL = lambda: list(map(int, input().split()))
    
    n = I()
    x, y = IL()
    print('White' if max(x-1, y-1) <= max(n-x, n-y) else 'Black')