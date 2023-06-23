def program4013():
    d, k, a, b, t u = map(int, input().split())
    
    t1 = d * b
    t2 = d * a + ((d - 1) // k) * t
    t3 = max(0, d - k) * b + min(k, d) * a
    dd = d % k
    d1 = d - dd
    u = d1 * a + max(0, (d1 // k - 1) * t)
    
    print(min([t1, t2, t3]))