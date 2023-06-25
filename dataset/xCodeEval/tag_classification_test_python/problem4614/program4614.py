def program4614():
    from string import ascii_uppercase
    n, k = map(int, input().split())
    s = input().strip()
    st =[]
    for c in ascii_uppercase:
        b = s.find(c)
        if b != -1:
            e = s.rfind(c)
            st.append((b, -1))
            st.append((e, 1))
    st.sort()
    ans = "NO"
    c = 0
    for i in st:
        c -= i[1]
        if c > k:
            ans = "YES"
            break
    print(ans)