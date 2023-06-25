def program200():
    string=input()
    a=len(string)-1
    b=0
    c=0
    while a>=0:
        if string[a]=='-':
            b=b+1
        if string[a]=='o':
            c=c+1
        a=a-1
    if c==0 or b%c==0:
        print("YES")
    else:
        print("NO")