def program3687():
    
    a, b, r = map(int, input().split())
    
    if a < 2 * r or b < 2 * r:
        print("Second")
    else:
        print("First")