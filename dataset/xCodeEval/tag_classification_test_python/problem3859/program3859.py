def program3859():
    n=int(input())
    a=input().split('W')
    v=[len(x) for x in a if len(x)>0]
    print(len(v))
    print(*v)