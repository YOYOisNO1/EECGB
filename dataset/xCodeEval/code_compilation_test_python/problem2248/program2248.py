def program2248():
    int a, b, c, d = tuple(map(int, input().split()))
    int x, y = tuple(map(int, input().split()))
    
    print(['NO', 'YES'][int(a%x == c%x and b%y == d%y)])