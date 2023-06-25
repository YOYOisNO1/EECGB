def program5997():
    a,b,c,d,e,f = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    s1 = a + b
    s2 = a + c
    s3 = a + d
    s4 = a + e
    s5 = a + f
    s6 = b + c
    s7 = b + d
    s8 = b + e
    s9 = b + f
    s10 = c + d
    s11 = c + e
    s12 = c + f
    s13 = d + e
    s14 = d + f
    s15 = e + f
    
    if a+s6 == s13 + f:
        print("YES")
    elif a+s7 == s11 + f:
        print("YES")
    elif a+s8 == s10 + f:
        print("YES")
    elif a+s9 == s10 + e:
        print("YES")
    elif a+s10 == s8 + f:
        print("YES")
    elif a+s11 == s7 + f:
        print("YES")
    elif a+s12 == s7 + e:
        print("YES")
    elif a+s13 == s6 + f:
        print("YES")
    elif a+s14 == s6 + e:
        print("YES")
    elif a+s15 == s6 + d:
        print("YES")
    else:
        print("NO")