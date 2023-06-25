def program739():
    import itertools
    
    n, m = map(int, input().split())
    
    st = []
    rv = []
    for num in range(1, n):
        pwr = (1 << (n-num-1))
        if ( m <= pwr ):
            st.append(num)
        else:
            rv.append(num)
            m -= pwr
    
    st.append(n)
    
    st.extend(reversed(rv))
    
    print(' ').join(map(str, st))