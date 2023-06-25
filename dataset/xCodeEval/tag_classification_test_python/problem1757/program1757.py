def program1757():
    from itertools import chain
    
    n = int(input())
    a = [int(a_i) for a_i in input().split()]
    ones = [[0]*n for i in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            ones[i][j] = sum(a) - a[i:j+1].count(1) + a[i:j+1].count(0)
    
    print(max(list(chain(*ones))))