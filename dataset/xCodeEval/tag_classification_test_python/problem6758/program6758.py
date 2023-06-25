def program6758():
    [d, k, a, b, t] = [int(x) for x in input().split()]
    
    time = min(d, k) * a
    d -= k
    
    if d > k:
        if t + a * k > b * k:
            time += (d - (d % k)) * b
        else:
            time += (d - (d % k)) * a + d // k * t
        d = d % k
    
    if d <= 0:
        print(time)
    else:
        if t + a * d > b * d:
            time += d * b
        else:
            time += d * a + t
        print(time)