def program2725():
    n = input()
     ja = [0] * n
    b = [0] * n
    for i in range (n) :
        a[i] , b[i] = map(int , input().split())
    ans = 0
    for i in range (n) :
        for j in range (n) :
            if a[i] == b[j] and i != j : ans += 1
    print ans