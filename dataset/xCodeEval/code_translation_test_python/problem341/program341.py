def program341():
    n = int(input())
    s = input()
    
    groups = [set('4567890'), set('1234568'), set('235689'), set('124578')]
    
    ans = True
    
    for group in groups:
        if all(c in group for c in s):
            ans = False
    
    print('YES' if ans else 'NO')