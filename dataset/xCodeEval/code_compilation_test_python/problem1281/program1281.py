def program1281():
    n,m=map(int,input().split())
    s=list(map(int,input().split())
    p=list(map(int,input().split())
    k=""
    for i in s:
        if i in p:
            k+=str(i)+" "
    print(k)