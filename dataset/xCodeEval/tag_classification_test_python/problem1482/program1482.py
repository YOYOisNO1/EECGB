def program1482():
    a=list((str.lower(input())))
    b=len(a)
    c=[]
    d=["a","o","y","e","u","i"]
    for i in range(b):
        if a[i] in d:
            pass
        else:
            c.append('.')
            c.append(a[i])
    print(''.join(c))