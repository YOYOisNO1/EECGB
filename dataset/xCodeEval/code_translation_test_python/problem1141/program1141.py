def program1141():
    #here
    n = int(input())
    a = map(int, input().split())
    
    ones = a.count(1)
    
    ma = 0
    for i in range(0, n):
        for j in range(i, n):
            seg = [a[k] for k in range(i, j+1)]
            unos = ones - seg.count(1) + seg.count(0)
            if unos > ma:
                ma = unos 
    
    print(ma)