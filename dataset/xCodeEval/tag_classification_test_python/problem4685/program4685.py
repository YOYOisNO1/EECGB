def program4685():
    n , k = map(int,input().split())
    s = input()
    
    d = {}
    for i in range(n):
        d[s[i]] =i
    
    st = set()
    f =  False
    
    for i in range(n):
        st.add(s[i])
        if len(st) > k :
            f = True
            break
        if d[s[i]] == i :
            st.remove(s[i])
    
    if f :
        print('YES')
    else:
        print('NO')