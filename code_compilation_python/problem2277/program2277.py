def program2277():
    a, k = input(), 0
    for i in range(len(a)//2): 
        if a[i] != a[len(a)-i-1]: 
            k += 1
    if k > 1: print('NO')
    elif k == 0, len(a)%2 == 0: print('NO')
    else: print('YES')