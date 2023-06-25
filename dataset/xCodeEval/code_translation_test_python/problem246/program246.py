def program246():
    k2, k3, k5, k6 = map(int, input().split())
    
    A = min(k2, k5, k6)
    B = min(k3, k2 - A)
    
    print(256) * A + 32 * B