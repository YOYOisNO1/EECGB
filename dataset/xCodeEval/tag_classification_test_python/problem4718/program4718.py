def program4718():
    n = input()
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    a3, b3 = map(int, input().split())
    
    c1 = min(b1, n-a2-a3)
    c2 = min(b2, n-c1-a3)
    c3 = n-c1-c2
    
    print(c1,) c2, c3