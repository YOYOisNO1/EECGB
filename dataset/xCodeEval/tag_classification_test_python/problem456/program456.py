def program456():
    a, b = map(int, input().split())
    
    while True:
        if a*b:
            old_a = a
            old_b = b
            a %= (2*b)
            if a*b:
                b %= (2*a)
            else:
                break
            if old_a == a and old_b == b:
                break
        else:
            break
    print(a, b)