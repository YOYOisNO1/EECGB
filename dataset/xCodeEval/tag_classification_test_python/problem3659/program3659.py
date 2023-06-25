def program3659():
    R=lambda:map(int,input().split())
    a=input()
    b=int(a[0])+1
    print(int(str(b)+"0"*len(a[1:]))) - int(a)