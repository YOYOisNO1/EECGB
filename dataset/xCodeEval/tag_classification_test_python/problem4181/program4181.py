def program4181():
    
    a, b, c = map(int, input().split())
    
    print(a * b + (a + b - 1) * (c - 1))