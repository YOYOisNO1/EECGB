def program2498():
    n=int(input())
    s=list(input())
    b=0
    c=0
    for i in range(n):
        if(s[i]=='0'):
            b=b+1;
        else:
            c=c+1
    if(b!=c):
        print("1")
        for i in range(n):
        print(s[i],end="")
    else:
        print("2")
        for i in range(n-1):
            print(s[i],end="")
        print(" ",end="")
        print(s[n-1])