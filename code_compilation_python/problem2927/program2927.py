def program2927():
    n = int(input())
    
    a = n / 36
    b = (n - a * 36) / 3
    if n - a * 36 - b * 3 == 2:
        b += 1
    
    print a, b