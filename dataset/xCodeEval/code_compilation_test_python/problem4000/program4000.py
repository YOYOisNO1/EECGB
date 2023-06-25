def program4000():
    n, m, m1, m2 = map(int, input().split())
    a = map(int, input())
    s = "Correct"
    if n==2:
        if (a[0]!=m1 and a[0]!=m2) : s = "Incorrect"
    for i in a:
        if (i<m1) or (i>m2): s = "Incorrect"
    print s