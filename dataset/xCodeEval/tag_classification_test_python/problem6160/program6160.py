def program6160():
    r = lambda: map(int, input().split())
    
    r1, c1, r2, c2 = r()
    print((r1) != r2) + (c1 != c2),
    print(0) if (r1 + c1) % 2 != (r2 + c2) % 2 else (r1 + c1 != r2 + c2) + (r1 - c1 != r2 - c2),
    print(max(abs(r1) - r2), abs(c1 - c2))