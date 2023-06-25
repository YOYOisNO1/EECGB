def program1020():
    n, m = [int(x) for x in range input().split()]
    
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
    if n not in prime or m not in prime:
        print('NO')
    elif prime.index(n) == prime.index(m) - 1:
        print('YES')
    else:
        print('NO')