def program4386():
    a=input()
    b=a[1:len(a)-1].replace('dot','.')
    b=a[0]+b
    if len(a)!=1:b+=a[-1]
    k=b[1:len(b)-1].replace('at','@',1)
    k=b[0]+k
    if len(b)!=1:k+=b[-1]
    print(k)