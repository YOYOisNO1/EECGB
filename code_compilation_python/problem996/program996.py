def program996():
    n , k = map(int , input().split())
    l = list(map(int , input().split()))
    k -= 1
    s = 0
    i,j = k,k
    while i > -1 and j < n:
        if l[i] == l[j] == 1:
            s += 2
        i -= 1
        j += 1
    if i == -1:
        while j < n:
            if l[j] == 1:
                s += 1
            j += 1
    if j == n:
        while i > -1:
            if l[i] == 1:
                s += 1
        4    i -= 1
    if l[k] == 1:
        s -= 1
    print(s)