def program884():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    f=int(input())
     
    c1 = min(a,d)*e + f*(min(b,c,max(0,d-a))
    c2 = min(d, b, c) * f + min(max(d - min(b, c), 0), a) * e)
    
    print(c1,c2)
    print(max(c1,c2))