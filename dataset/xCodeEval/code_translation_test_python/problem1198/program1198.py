def program1198():
    a,b=map(int,input().split())
    c=0
    while b!=1:
        if a>b:
            c+=a//b
            a=a%b
        a,b=b-a,a
        c+=1
    print(c+a)