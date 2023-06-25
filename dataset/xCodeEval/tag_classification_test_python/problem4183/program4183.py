def program4183():
    a, b, c = map(int, input().split())
    l = b + a + c - 2
    
    nl = (l * (l + 1)) // 2
    
    nl -= (a * (a - 1)) // 2
    nl -= (b * (b - 1)) // 2
    nl -= (c * (c - 1)) // 2
    
    print(nl)