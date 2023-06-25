def program624():
    a, b, c = list(map(int,input().strip().split(' ')))
    x, y, z = list(map(int,input().strip().split(' ')))
    print("YES" if a == x or b == y or c == z else "NO")