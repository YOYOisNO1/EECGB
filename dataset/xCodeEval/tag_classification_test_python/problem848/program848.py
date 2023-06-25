def program848():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=set(map(int,input().split()))
    o=''
    for i in a:
        if i in b:
            o+=str(i)+' '
    print(o)