def program3819():
    z=input()
    s=set(i for i in z if i>"?")
    c=z.count("?")
    q=1
    if z[0]=="?":c-=1;q=9
    for i in range(len(s)):q*=10-i-((i<1)*(z[0]>"?"))
    print`q`+"0"*c
    