def program791():
    a, b = [int(value) for value in input().split(' ')]
    
    year = 0
    
    while a <= b:
        a *= 3
        b *= 2
        year += 1
        
    print(year)