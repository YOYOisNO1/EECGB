def program3863():
    n,k=map(int,input().split())
    l=list(input())
    y=list(set(l))
    x=[]
    for i in range(len(y)):
        x.append(l.count(y[i]))
    for i in range(len(x)):
        if x[i]>k:
            print("NO")
            break
    else:
        print("YES")