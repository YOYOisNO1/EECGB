def program269():
    n, t, k, d = input().split()
    n, t, k, d = int(n), int(t), int(k), int(d)
    sk = 0
    st = 0
    sk1 = k
    m = abs(k - d)
    st1 = m
    
    while sk <= n:
        sk += k
        st += t
    
    while sk1 <= n :
         sk1 = 2*k
         st1 += 2*t
    
    if st < st1:
        print('NO')
    else:
        print('YES')