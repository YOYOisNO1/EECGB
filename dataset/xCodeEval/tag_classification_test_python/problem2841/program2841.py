def program2841():
    l=input()/2
    S=input()
    x=S.count("x")
    f,s="XxX"[x>l:(x>l)+2]
    m=abs(l-x)
    print(m,S.replace(f,s,m))