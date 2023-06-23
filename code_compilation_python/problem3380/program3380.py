def f(s):
        return s==s[-1::-1]
    a,b=input().split(':')
    p,q=int(a),int(b)
    c=0
    while not f(a+b):
        temp=q+1//60
        q=(q+1)%60
        p=(p+temp)%24
        c+=1
        a,b=str(p),str(q)
        if len(a)==1:
            a='0'+a
        if len(b)==1:
            b='0'+b
    print(c)