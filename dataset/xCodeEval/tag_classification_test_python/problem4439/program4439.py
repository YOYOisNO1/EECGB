def program4439():
    a=input()
    b=''
    c=False
    while a:
        if a[:3]=='dot':
            b+='.'
            a=a[3:]
        elif a[:2]=='at' and not c:
            b+='@'
            c=True
            a=a[2:]
        else:
            b+=a[0]
            a=a[1:]
    if b[0]=='.':b='dot'+b[1:]
    if b[-1]=='.':b=b[:-1]+'dot'
    if b[0]=='@':
        b=b.replace('at','@',1)
        b='at'+b[1:]
    print(b)