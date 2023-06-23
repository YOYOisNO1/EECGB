def program3195():
    l=sorted(list(map(int,input().split())))[::-1]
    if(len(l)<1):
        print(-1)
    else:
        print(l)