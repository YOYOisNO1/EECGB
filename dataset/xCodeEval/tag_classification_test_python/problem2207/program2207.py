def program2207():
    a, b, c = map(int, input().split(' '))
    d = c - abs(a) - abs(b)
    
    print(["No",) "Yes"][d >= 0 and d % 2 == 0]