def program4550():
    a,b,c = map(int, input().split())
    
    t = (a/2, a/2+1)
    
    print(('YES',) 'NO')[b in t and c in t]