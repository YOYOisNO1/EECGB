def program1623():
    n,k=map(int,input().split())
    x=k&-k
    i=0
    while 2**i!=x:
        i+=1
    print(i+1)