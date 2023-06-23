def program907():
    a1 = int(input())
    a2 = int(input())
    k1 = int(input())
    k2 = int(input())
    n = int(input())
    
    min = 0
    if a1*(k1-1) + a2*(k2-1) >= n:
        print("test1")
        min=0
    else:
        print("test2")
        leftover = n
        leftover -= a1*(k1-1) + a2*(k2-1)
        min += leftover
    
    max=0
    if k1<k2:
        leftover = n
        if n/k1 > a1:
            max += a1
            leftover -= a1*k1
            max += int(leftover/k2)
        else:
            max = int(n/k1)
    else:
        leftover = n
        if n/k2 > a2:
            max += a2
            leftover -= a2*k2
            max += int(leftover/k1)
        else:
            max = int(n/k2)
    
    print(min)
    print(/n)
    print(max)