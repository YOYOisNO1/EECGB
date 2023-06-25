def program267():
    n, t, k, d = input().split()
    n, t, k, d = int(n), int(t), int(k), int(d)
    sk: int = 0
    st = 0
    sk1 = k
    st1 = abs(k - d)
    
    while (sk <= n) or (sk1 <= n):
        sk += k
        st += t
        sk1 = 2*k
        st1 += 2*t
    if st < st1:
        print('NO')
    else:
        print('YES')