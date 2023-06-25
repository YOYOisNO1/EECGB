def program960():
    x, y=list(map(int, input().split()))
    if y-1>x or (x==1 and y==0) or (y==1 and x!=0) or y==0 or (x-y+1)%2!=0:
        print('No')
    else:
        print('Yes')