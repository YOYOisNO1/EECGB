def program1967():
    burger = input()
    Nb, Ns, Nc = map(int, input().split())
    Pb, Ps, Pc = map(int, input().split())
    r = int(input())
    
    B = burger.count('B')
    S = burger.count('S')
    C = burger.count('C')
    
    left = 0
    right = 10**14
    
    while(left < right):
        middle = (left + right + 1)//2
        
        b = max(middle * B - Nb, 0)
        s = max(middle * S - Ns, 0)
        c = max(middle * C - Nc, 0)
        
        if b * Pb + s * Ps + c * Pc > r:
            right = middle - 1
        else:
            left = middle
        
    print(right)