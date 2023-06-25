def program138():
    n= int(input())
    item = list(map(int, input().split()))
    s= sum(item)
    item.sort()
    a=((s/n)*10)%10
    if a>=5:
        t=(s//n) +1
    else:
        t=s//n
    for i in range(n+1):
        if t == 5:
            print(i)
            break
        else:
            item[i]=5
            s=sum(item)
            a=((s/n)*10)%10
            if a>=5:
                 t=(s//n) +1
            else:
                 t=s//n