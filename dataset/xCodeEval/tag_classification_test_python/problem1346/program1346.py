def program1346():
    n=input()
    
    l=lambda:map(int,input().split())
    a=l()[1:]
    b=l()[1:]
    c=0
    R=set()
    while a and b:
        c+=1
        A = a.pop(0)
        B = b.pop(0)
        if A > B:
            a += [B,A]
        else:
            b += [A,B] 
        r=(tuple(a),tuple(b))
        if r in R:
            print(-1)
            exit(0)
        R.add(r)
    
    print(c,) 1 if a else 2