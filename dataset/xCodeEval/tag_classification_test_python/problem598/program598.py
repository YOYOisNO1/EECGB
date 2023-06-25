def program598():
    l=sorted(list(map(int,input().split())))
    if l[2]>(l[0]+l[1])*2:
        print(l[0]+l[1])
    else:
        print((l[0]+l[1]+l[2])//3)