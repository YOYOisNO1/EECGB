def program3507():
    h1,m1 = map(int,input().split(":"))
    h2,m2 = map(int,input().split(":"))
    m_m = ((h2-h1)*60 + (m2-m1))//2
    m = m1 + m_m % 60
    h = h1 + m_m // 60 + m // 60
    m = m % 60
    print(h//10,h%10,":",m//10,m%10,sep = "")