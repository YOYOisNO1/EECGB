def program6205():
    a, c, b, d = map (int, input().split())
    
    print(2) - int (a == b or c == d), 1 if abs (a - b) == abs (c - d) else 2 * ((a + b + c + d + 1) % 2), max (abs (a - b), abs (c - d))