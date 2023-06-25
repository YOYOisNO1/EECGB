def program943():
    y=int(input())
    x=list(map(int,input().split()))
    c=0
    d=0
    for i in range(y-1):
        if x[i]=='S' and x[i+1]=='F':
            c=c+1
        elif x[i]=='F' and x[i+1]=='S':
            d=d+1
        
    elif c>d:
        print("YES")
    else:
        print("NO")