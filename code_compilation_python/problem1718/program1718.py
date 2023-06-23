def program1718():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    
    _b = int(b);
    b -= c
    
    t = 0
    if(n >= b) t = 1
    
    print(max(n // a, (n - _b) // b + max(t, ((n - _b) % n + _b) // a)))