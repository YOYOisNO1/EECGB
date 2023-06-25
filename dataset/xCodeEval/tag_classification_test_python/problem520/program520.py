def program520():
    (n,m,a) = map(int, input().split())
    print(((m/a) + (0 if m%a == 0 else 1))*(n/a + (0 if n%a == 0 else 1)))